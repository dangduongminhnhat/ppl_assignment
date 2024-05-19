from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class FuncZcode(Type):
    def __init__(self, param=[], typ=None, body=False):
        self.param = param
        self.typ = typ
        self.body = body


class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.block_for = 0
        self.return_visited = False  # True if return statement is visited
        self.return_function = None
        self.list_functions = {
            "readNumber": FuncZcode([], NumberType(), True),
            "readBool": FuncZcode([], BoolType(), True),
            "readString": FuncZcode([], StringType(), True),
            "writeNumber": FuncZcode([NumberType()], VoidType(), True),
            "writeBool": FuncZcode([BoolType()], VoidType(), True),
            "writeString": FuncZcode([StringType()], VoidType(), True)
        }
        self.global_envi = [{}]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def infer(self, item, typ, param):
        if type(item) is CallExpr:
            self.list_functions[item.name.name].typ = typ
        else:
            for env in param:
                if item.name in env:
                    env[item.name] = typ

    def check_type(self, ltype, rtype):
        if not type(ltype) is type(rtype):
            return False
        if type(ltype) is ArrayType:
            if len(ltype.size) != len(rtype.size) or type(ltype.eleType) != type(rtype.eleType):
                return False
            for i in range(len(ltype.size)):
                if ltype.size[i] != rtype.size[i]:
                    return False
        return True

    def visitProgram(self, ast: Program, param):
        for decl in ast.decl:
            self.visit(decl, param)
        for func_name in self.list_functions:
            if not self.list_functions[func_name].body:
                raise NoDefinition(func_name)
        if not "main" in self.list_functions:
            raise NoEntryPoint()
        else:
            method = self.list_functions["main"]
            if len(method.param) > 0 or type(method.typ) is not VoidType:
                raise NoEntryPoint()

    def visitVarDecl(self, ast: VarDecl, param):
        if ast.name.name in param[0]:
            raise Redeclared(Variable(), ast.name.name)
        param[0][ast.name.name] = None
        if ast.varInit:
            typ = self.visit(ast.varInit, param)
            if type(typ) is FuncZcode:
                if ast.varType:
                    varType = self.visit(ast.varType, param)
                    self.infer(ast.varInit, varType, param)
                else:
                    raise TypeCannotBeInferred(ast)
            else:
                if ast.varType:
                    varType = self.visit(ast.varType, param)
                    if typ is None:
                        self.infer(ast.varInit, varType, param)
                    elif type(typ) is ArrayType and typ.eleType is None:
                        check = self.infer_array(ast.varInit, varType, param)
                        if check == False:
                            raise TypeCannotBeInferred(ast)
                    elif not self.check_type(varType, typ):
                        raise TypeMismatchInStatement(ast)
                    typ = varType
                else:
                    if typ is None:
                        raise TypeCannotBeInferred(ast)
                    elif type(typ) is ArrayType and typ.eleType is None:
                        raise TypeCannotBeInferred(ast)
        else:
            if ast.varType:
                typ = self.visit(ast.varType, param)
            else:
                typ = None
        param[0][ast.name.name] = typ
        return typ

    def visitFuncDecl(self, ast: FuncDecl, param):
        if ast.name.name in self.list_functions:
            if self.list_functions[ast.name.name].body or ast.body is None:
                raise Redeclared(Function(), ast.name.name)
        list_param = {}
        type_param = []
        env = [list_param] + param
        for decl in ast.param:
            try:
                type_param.append(self.visit(decl, env))
            except Exception as e:
                if ast.body:
                    raise Redeclared(Parameter(), e.name)
                else:
                    type_param.append(decl.varType)

        if ast.body is None:
            self.list_functions[ast.name.name] = FuncZcode(
                type_param, None, False)
            return
        if ast.name.name in self.list_functions:
            para = self.list_functions[ast.name.name].param
            if len(para) != len(type_param):
                raise Redeclared(Function(), ast.name.name)
            for i in range(len(para)):
                if type(para[i]) != type(type_param[i]):
                    raise Redeclared(Function(), ast.name.name)
            self.list_functions[ast.name.name].body = True
        self.return_visited = False
        self.visit(ast.body, env)
        if self.return_visited:
            if ast.name.name in self.list_functions:
                method = self.list_functions[ast.name.name]
                if method.typ is None and self.return_function["type"] is None:
                    raise TypeCannotBeInferred(self.return_function["stmt"])
                elif method.typ is None:
                    if type(self.return_function["type"]) is ArrayType and self.return_function["type"].eleType is None:
                        raise TypeCannotBeInferred(
                            self.return_function["stmt"])
                    self.list_functions[ast.name.name].typ = self.return_function["type"]
                elif self.return_function["type"] is None:
                    raise TypeCannotBeInferred(self.return_function["stmt"])
                elif type(self.return_function["type"]) is ArrayType and self.return_function["type"].eleType is None:
                    raise TypeCannotBeInferred(self.return_function["stmt"])
                elif not self.check_type(self.return_function["type"], self.list_functions[ast.name.name].typ):
                    raise TypeMismatchInStatement(self.return_function["stmt"])
            else:
                method_type = self.return_function["type"]
                if method_type is None:
                    raise TypeCannotBeInferred(self.return_function["stmt"])
                elif type(method_type) is ArrayType and method_type.eleType is None:
                    raise TypeCannotBeInferred(self.return_function["stmt"])
                self.list_functions[ast.name.name] = FuncZcode(
                    type_param, self.return_function["type"], True)
        else:
            if ast.name.name in self.list_functions:
                if self.list_functions[ast.name.name].typ is not None and type(self.list_functions[ast.name.name].typ) is not VoidType:
                    raise TypeMismatchInStatement(Return(None))
            self.list_functions[ast.name.name] = FuncZcode(
                type_param, VoidType(), True)
        self.return_function = None
        self.return_visited = False

    def visitNumberType(self, ast, param): return NumberType()
    def visitBoolType(self, ast, param): return BoolType()
    def visitStringType(self, ast, param): return StringType()
    def visitArrayType(self, ast: ArrayType, param): return ast

    def visitBinaryOp(self, ast: BinaryOp, param):
        ltype = self.visit(ast.left, param)
        if type(ltype) is FuncZcode:
            ltype = ltype.typ
        if ast.op in ["+", "-", "*", "/", "%"]:
            if ltype is None:
                self.infer(ast.left, NumberType(), param)
                ltype = NumberType()
        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            if ltype is None:
                self.infer(ast.left, NumberType(), param)
                ltype = NumberType()
        elif ast.op in ['and', 'or']:
            if ltype is None:
                self.infer(ast.left, BoolType(), param)
                ltype = BoolType()
        elif ast.op == "==":
            if ltype is None:
                self.infer(ast.left, StringType(), param)
                ltype = StringType()
        elif ast.op == "...":
            if ltype is None:
                self.infer(ast.left, StringType(), param)
                ltype = StringType()
        rtype = self.visit(ast.right, param)
        if type(rtype) is FuncZcode:
            rtype = rtype.typ
        if ast.op in ["+", "-", "*", "/", "%"]:
            if rtype is None:
                self.infer(ast.right, NumberType(), param)
                rtype = NumberType()
            if type(ltype) in [BoolType, StringType] or type(rtype) in [BoolType, StringType]:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            if rtype is None:
                self.infer(ast.right, NumberType(), param)
                rtype = NumberType()
            if type(ltype) in [BoolType, StringType] or type(rtype) in [BoolType, StringType]:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op in ['and', 'or']:
            if rtype is None:
                self.infer(ast.right, BoolType(), param)
                rtype = BoolType()
            if not (type(ltype) is BoolType) or not (type(rtype) is BoolType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op == "==":
            if rtype is None:
                self.infer(ast.right, StringType(), param)
                rtype = StringType()
            if not (type(ltype) is StringType) or not (type(rtype) is StringType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op == "...":
            if rtype is None:
                self.infer(ast.right, StringType(), param)
                rtype = StringType()
            if not (type(ltype) is StringType) or not (type(rtype) is StringType):
                raise TypeMismatchInExpression(ast)
            return StringType()

    def visitUnaryOp(self, ast: UnaryOp, param):
        operand_type = self.visit(ast.operand, param)
        if type(operand_type) is FuncZcode:
            operand_type = operand_type.typ
        if ast.op == "-":
            if operand_type is None:
                self.infer(ast.operand, NumberType(), param)
            elif not (type(operand_type) is NumberType):
                raise TypeMismatchInExpression(ast)
            return NumberType()
        elif ast.op == "not":
            if operand_type is None:
                self.infer(ast.operand, NumberType(), param)
            elif not (type(operand_type) is BoolType):
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitCallExpr(self, ast: CallExpr, param):
        if not ast.name.name in self.list_functions:
            raise Undeclared(Function(), ast.name.name)
        method = self.list_functions[ast.name.name]
        if len(method.param) != len(ast.args):
            raise TypeMismatchInExpression(ast)
        for i in range(len(method.param)):
            typ = self.visit(ast.args[i], param)
            if typ is None:
                self.infer(ast.args[i], method.param[i], param)
            elif type(typ) is ArrayType and typ.eleType is None:
                check = self.infer_array(ast.args[i], method.param[i], param)
                if check == False:
                    raise TypeMismatchInExpression(ast.args[i])
            elif not self.check_type(typ, method.param[i]):
                raise TypeMismatchInExpression(ast)
        if type(method.typ) is VoidType:
            raise TypeMismatchInExpression(ast)
        return method.typ

    def visitId(self, ast: Id, param):
        for env in param:
            if ast.name in env:
                return env[ast.name]
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast: ArrayCell, param):
        typ = self.visit(ast.arr, param)
        if typ is None:
            raise TypeMismatchInExpression(ast)
        else:
            if type(typ) is not ArrayType:
                raise TypeMismatchInExpression(ast)
            for expr in ast.idx:
                typ_expr = self.visit(expr, param)
                if typ_expr is None:
                    self.infer(expr, NumberType(), param)
                    typ_expr = NumberType()
                if type(typ_expr) is not NumberType:
                    raise TypeMismatchInExpression(ast)
            if len(typ.size) < len(ast.idx):
                raise TypeMismatchInExpression(ast)
            elif len(typ.size) == len(ast.idx):
                return typ.eleType
            else:
                return ArrayType(typ.size[len(ast.idx):], typ.eleType)

    def visitBlock(self, ast: Block, param):
        env = [{}] + param
        for stmt in ast.stmt:
            self.visit(stmt, env)

    def visitIf(self, ast: If, param):
        type_expr = self.visit(ast.expr, param)
        if type_expr is None:
            self.infer(ast.expr, BoolType(), param)
        elif not (type(type_expr) is BoolType):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, param)
        for expr, stmt in ast.elifStmt:
            typ = self.visit(expr, param)
            if typ is None:
                self.infer(ast.expr, BoolType(), param)
            elif not (type(typ) is BoolType):
                raise TypeMismatchInStatement(ast)
            self.visit(stmt, param)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)

    def visitFor(self, ast: For, param):
        id_type = self.visit(ast.name, param)
        if id_type is None:
            self.infer(ast.name, NumberType(), param)
        elif type(id_type) is not NumberType:
            raise TypeMismatchInStatement(ast)
        cond_type = self.visit(ast.condExpr, param)
        if cond_type is None:
            self.infer(ast.condExpr, BoolType(), param)
        elif type(cond_type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        upd_type = self.visit(ast.updExpr, param)
        if upd_type is None:
            self.infer(ast.updExpr, NumberType(), param)
        elif type(upd_type) is not NumberType:
            raise TypeMismatchInStatement(ast)
        self.block_for += 1
        self.visit(ast.body, param)
        self.block_for -= 1

    def visitContinue(self, ast, param):
        if self.block_for == 0:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if self.block_for == 0:
            raise MustInLoop(ast)

    def visitReturn(self, ast: Return, param):
        if not self.return_visited:
            self.return_visited = True
            if ast.expr is None:
                self.return_function = {"stmt": ast, "type": VoidType()}
            else:
                typ = self.visit(ast.expr, param)
                if typ is None:
                    raise TypeCannotBeInferred(ast)
                if type(typ) is ArrayType and typ.eleType is None:
                    raise TypeCannotBeInferred(ast)
                self.return_function = {"stmt": ast, "type": typ}
        else:
            if ast.expr is None:
                if type(self.return_function["type"]) is not VoidType:
                    raise TypeMismatchInStatement(ast)
            else:
                typ = self.visit(ast.expr, param)
                if typ is None:
                    self.infer(ast.expr, self.return_function["type"], param)
                elif type(typ) is ArrayType and typ.eleType is None:
                    self.infer_array(
                        ast.expr, self.return_function["type"], param)
                elif not self.check_type(typ, self.return_function["type"]):
                    raise TypeMismatchInStatement(ast)

    def visitAssign(self, ast: Assign, param):
        rtype = self.visit(ast.rhs, param)
        ltype = self.visit(ast.lhs, param)
        if ltype is None and rtype is None:
            raise TypeCannotBeInferred(ast)
        elif ltype is None:
            if type(rtype) is ArrayType and rtype.eleType is None:
                raise TypeCannotBeInferred(ast)
            self.infer(ast.lhs, rtype, param)
        elif rtype is None:
            if type(ltype) is ArrayType and ltype.eleType is None:
                raise TypeCannotBeInferred(ast)
            self.infer(ast.rhs, ltype, param)
        else:
            if type(ltype) is ArrayType and type(rtype) is ArrayType:
                if ltype.eleType is None and rtype.eleType is None:
                    raise TypeCannotBeInferred(ast)
                elif ltype.eleType is None:
                    check = self.infer_array(ast.lhs, rtype, param)
                    if check == False:
                        raise TypeMismatchInStatement(ast)
                elif rtype.eleType is None:
                    check = self.infer_array(ast.rhs, ltype, param)
                    if check == False:
                        raise TypeMismatchInStatement(ast)
                elif not self.check_type(ltype, rtype):
                    raise TypeMismatchInStatement(ast)
            elif not self.check_type(ltype, rtype):
                raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, param):
        if not ast.name.name in self.list_functions:
            raise Undeclared(Function(), ast.name.name)
        method = self.list_functions[ast.name.name]
        if len(method.param) != len(ast.args):
            raise TypeMismatchInStatement(ast)
        for i in range(len(method.param)):
            typ = self.visit(ast.args[i], param)
            if typ is None:
                self.infer(ast.args[i], method.param[i], param)
            elif type(typ) is ArrayType and typ.eleType is None:
                if type(method.param[i]) is not ArrayType:
                    raise TypeMismatchInStatement(ast)
                else:
                    check = self.infer_array(
                        ast.args[i], method.param[i], param)
                    if check == False:
                        raise TypeMismatchInExpression(ast.args[i])
            elif not self.check_type(typ, method.param[i]):
                raise TypeMismatchInStatement(ast)
        if method.typ is None:
            method.typ = VoidType()
        if type(method.typ) is not VoidType:
            raise TypeMismatchInStatement(ast)
        return method.typ

    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()

    def infer_array(self, item, typ, param):
        if type(typ) is ArrayType:
            if type(item) is ArrayLiteral:
                if int(typ.size[0]) != len(item.value):
                    return False
                else:
                    if len(typ.size) > 1:
                        eleType = ArrayType(typ.size[1:], typ.eleType)
                    else:
                        eleType = typ.eleType
                    for val in item.value:
                        val_type = self.visit(val, param)
                        if val_type is None:
                            check = self.infer_array(val, eleType, param)
                            if check == False:
                                return False
                        elif type(val_type) is ArrayType and val_type.eleType is None:
                            check = self.infer_array(val, eleType, param)
                            if check == False:
                                return False
                        elif not self.check_type(val_type, eleType):
                            return False
                    return True
            else:
                self.infer(item, typ, param)
                return True
        else:
            if type(item) is ArrayLiteral:
                return False
            self.infer(item, typ, param)
            return True

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        typ = self.visit(ast.value[0], param)
        for i in range(1, len(ast.value)):
            typ_expr = self.visit(ast.value[i], param)
            if typ is None:
                typ = typ_expr
            elif type(typ) is ArrayType:
                if typ.eleType is None:
                    typ = typ_expr
            if typ_expr is not None:
                if type(typ_expr) is ArrayType and typ_expr.eleType is None:
                    continue
                else:
                    if not self.check_type(typ, typ_expr):
                        raise TypeMismatchInExpression(ast)
        if typ is not None:
            if type(typ) is ArrayType and typ.eleType is None:
                return ArrayType([float(len(ast.value))], None)
            else:
                for val in ast.value:
                    typ_expr = self.visit(val, param)
                    if typ_expr is None:
                        self.infer(val, typ, param)
                    elif type(typ_expr) is ArrayType and typ_expr.eleType is None:
                        check = self.infer_array(val, typ, param)
                        if not check:
                            raise TypeMismatchInExpression(ast)
                    elif not self.check_type(typ, typ_expr):
                        raise TypeMismatchInExpression(ast)
                if type(typ) is ArrayType:
                    return ArrayType([float(len(ast.value))] + typ.size, typ.eleType)
                else:
                    return ArrayType([float(len(ast.value))], typ)
        return ArrayType([float(len(ast.value))], None)
