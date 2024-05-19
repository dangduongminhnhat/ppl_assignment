from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from Utils import *
from AST import *
# from src.main.zcode.utils.Visitor import *
# from src.main.zcode.utils.AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("writeNumber", MType(
                [NumberType()], VoidType()), CName(self.libName)),
            Symbol("writeBool", MType([BoolType()],
                   VoidType()), CName(self.libName)),
            Symbol("writeString", MType(
                [StringType()], VoidType()), CName(self.libName)),
            Symbol("readNumber", MType([], NumberType()), CName(self.libName)),
            Symbol("readBool", MType([], BoolType()), CName(self.libName)),
            Symbol("readString", MType([], StringType()), CName(self.libName))
        ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym, isGlobal=False):
        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=True):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.className = "ZCodeClass"
        self.path = path
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.checkType = CheckType(astTree)
        self.checkType.check()
        self.list_functions = self.checkType.list_functions
        self.return_visited = False

    # Done visitProgram
    def visitProgram(self, ctx: Program, c):
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        staticDecl = self.env
        main_func = None
        for x in ctx.decl:
            if type(x) is VarDecl:
                self.emit.printout(self.emit.emitATTRIBUTE(
                    x.name.name, x.varType, False, x.varInit))
                staticDecl = [
                    Symbol(x.name.name, x.varType, None)] + staticDecl

        env = [staticDecl]
        frame = Frame("<init>", VoidType)
        self.emit.printout(self.emit.emitMETHOD(
            lexeme="<init>", in_=MType([], VoidType()), isStatic=False, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(
        ), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR(
            "this", self.className, 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

        frame = Frame("<clinit>", VoidType)
        self.emit.printout(self.emit.emitMETHOD(
            lexeme="<clinit>", in_=MType([], VoidType()), isStatic=True, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for var in ctx.decl:
            if type(var) is VarDecl and var.varInit is not None:
                self.visit(Assign(var.name, var.varInit),
                           SubBody(frame, env, True))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

        e = SubBody(None, env, False)
        for decl in ctx.decl:
            if type(decl) is FuncDecl:
                if decl.name.name == "main" and decl.body:
                    main_func = decl
                elif decl.body:
                    self.visit(decl, e)

        frame = Frame("main", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="main", in_=MType(
            [ArrayType([1.0], StringType())], VoidType()), isStatic=True, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
            [], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        index = frame.getNewIndex()
        # typeParam = [VarZcode("for", NumberType(), index, True)]
        # self.emit.printout(self.emit.emitVAR(
        #     index, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.visit(main_func.body, SubBody(frame, env, False))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        self.emit.emitEPILOG()
        return c

    # Done visitVarDecl
    def visitVarDecl(self, ctx: VarDecl, o: SubBody):
        if o.isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(
                ctx.name.name, ctx.varType, False, ctx.varInit))
            o.sym[0] = [Symbol(ctx.name.name, ctx.varType, None)] + o.sym[0]
            if ctx.varInit:
                self.visit(Assign(ctx.name, ctx.varInit), o)
        else:
            index = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(
                index, ctx.name.name, ctx.varType, o.frame.startLabel[-1], o.frame.endLabel[-1], o.frame))
            o.sym[0] = [Symbol(ctx.name.name, ctx.varType,
                               Index(index))] + o.sym[0]
            if ctx.varInit:
                self.visit(Assign(ctx.name, ctx.varInit), o)

    # Done visitFuncDecl
    def visitFuncDecl(self, ctx: FuncDecl, o: SubBody):
        parttype = self.list_functions[ctx.name.name].param
        rettype = self.list_functions[ctx.name.name].typ
        frame = Frame(ctx.name.name, rettype)
        mtype = MType(parttype, rettype)
        self.emit.printout(self.emit.emitMETHOD(
            ctx.name.name, mtype, True, o.frame))
        frame.enterScope(True)
        self.return_visited = False
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        newSym = [[]] + o.sym
        for vardecl in ctx.param:
            self.visit(vardecl, SubBody(frame, newSym, False))
        self.visit(ctx.body, SubBody(frame, newSym))
        if self.return_visited == False:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        o.sym[0] = [Symbol(ctx.name.name, mtype,
                           CName(self.className))] + o.sym[0]

    def visitNumberType(self, ast, param):
        pass

    def visitBoolType(self, ast, param):
        pass

    def visitStringType(self, ast, param):
        pass

    def visitArrayType(self, ast, param):
        pass

    # Done visitBinaryOp
    def visitBinaryOp(self, ctx: BinaryOp, o: Access):
        left, t_left = self.visit(ctx.left, o)
        right, t_right = self.visit(ctx.right, o)

        if ctx.op in ["+", "-"]:
            code, rettype = left + right + \
                self.emit.emitADDOP(ctx.op, NumberType(),
                                    o.frame), NumberType()
        elif ctx.op in ["*", "/"]:
            code, rettype = left + right + \
                self.emit.emitMULOP(ctx.op, NumberType(),
                                    o.frame), NumberType()
        elif ctx.op == "%":
            code, rettype = left + right + \
                self.emit.emitMOD(o.frame), NumberType()
        elif ctx.op in ["=", "!=", "<", ">", ">=", "<="]:
            code, rettype = left + right + \
                self.emit.emitREOP(ctx.op, BoolType(), o.frame), BoolType()
        elif ctx.op == "and":
            code, rettype = left + right + \
                self.emit.emitANDOP(o.frame), BoolType()
        elif ctx.op == "or":
            code, rettype = left + right + \
                self.emit.emitOROP(o.frame), BoolType()
        elif ctx.op == "==":
            code, rettype = left + right + \
                self.emit.emitEQUALS(o.frame), BoolType()
        elif ctx.op == "...":
            code, rettype = left + right + \
                self.emit.emitCONCAT(o.frame), StringType()
        return code, rettype

    # Done visitUnaryop
    def visitUnaryOp(self, ctx: UnaryOp, o: Access):
        code, _ = self.visit(ctx.operand, o)
        if ctx.op == "-":
            code += self.emit.emitNEGOP(ctx.op, o.frame)
            rettype = NumberType()
        elif ctx.op == "not":
            code += self.emit.emitNOT(BoolType(), o.frame)
            rettype = BoolType()
        return code, rettype

    # Done visitCallExpr
    def visitCallExpr(self, ctx: CallExpr, o: Access):
        for env in o.sym:
            check = False
            for symbol in env:
                if ctx.name.name == symbol.name:
                    sym = symbol
                    check = True
                    break
            if check:
                break
        cname = sym.value.value
        ctype = sym.mtype

        paramsCode = ""
        for x in ctx.args:
            pCode, pType = self.visit(x, Access(o.frame, o.sym, False, True))
            paramsCode = paramsCode + pCode

        code = paramsCode + \
            self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, o.frame)
        return code, ctype.rettype

    # Done visitId
    def visitId(self, ctx: Id, o: Access):
        for env in o.sym:
            check = False
            for symbol in env:
                if ctx.name == symbol.name:
                    sym = symbol
                    check = True
                    break
            if check:
                break
        if (not o.isFirst) and o.isLeft:
            o.frame.push()
        # elif (not o.isFirst) and not o.isLeft:
        #     o.frame.pop()
        emitType = sym.mtype
        if sym.value is None:
            if o.isLeft:
                retCode = self.emit.emitPUTSTATIC(
                    self.className + "/" + sym.name, emitType, o.frame)
            else:
                retCode = self.emit.emitGETSTATIC(
                    self.className + "/" + sym.name, emitType, o.frame)
        else:
            if o.isLeft:
                retCode = self.emit.emitWRITEVAR(
                    sym.name, emitType, sym.value.value, o.frame)
            else:
                retCode = self.emit.emitREADVAR(
                    sym.name, emitType, sym.value.value, o.frame)
        return retCode, sym.mtype

    def visitArrayCell(self, ast, param):
        pass

    # Done visitBlock
    def visitBlock(self, ctx: Block, o: SubBody):
        symbolnew = [[]] + o.sym
        o.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(
            o.frame.getStartLabel(), o.frame))
        for item in ctx.stmt:
            self.visit(item, SubBody(o.frame, symbolnew, False))
        self.emit.printout(self.emit.emitLABEL(
            o.frame.getEndLabel(), o.frame))
        o.frame.exitScope()

    # Done visitIf
    def visitIf(self, ctx: If, o: SubBody):
        condition_access = Access(o.frame, o.sym, False, True)
        code, _ = self.visit(ctx.expr, condition_access)
        self.emit.printout(code)
        false_label = o.frame.getNewLabel()
        end_label = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(false_label, o.frame))
        self.visit(ctx.thenStmt, o)
        self.emit.printout(self.emit.emitGOTO(end_label, o.frame))
        self.emit.printout(self.emit.emitLABEL(false_label, o.frame))
        for expr, stmt in ctx.elifStmt:
            expr_code, _ = self.visit(
                expr, Access(o.frame, o.sym, isLeft=False))
            self.emit.printout(expr_code)
            elif_label = o.frame.getNewLabel()
            self.emit.printout(self.emit.emitIFFALSE(elif_label, o.frame))
            self.visit(stmt, o)
            self.emit.printout(self.emit.emitGOTO(end_label, o.frame))
            self.emit.printout(self.emit.emitLABEL(elif_label, o.frame))
        if ctx.elseStmt:
            self.visit(ctx.elseStmt, o)
        self.emit.printout(self.emit.emitLABEL(end_label, o.frame))

    # Done visitFor
    def visitFor(self, ctx: For, o: SubBody):
        start_label = o.frame.getNewLabel()
        end_label = o.frame.getNewLabel()
        o.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(start_label, o.frame))

        condExpr, _ = self.visit(
            ctx.condExpr, Access(o.frame, o.sym, False, True))
        self.emit.printout(
            condExpr + self.emit.emitIFTRUE(end_label, o.frame))

        self.visit(ctx.body, o)

        self.emit.printout(self.emit.emitLABEL(
            o.frame.getContinueLabel(), o.frame))
        upd, _ = self.visit(ctx.updExpr, Access(o.frame, o.sym, False, True))
        idx, typ = self.visit(ctx.name, Access(o.frame, o.sym, False, False))
        addop = self.emit.emitADDOP('+', typ, o.frame)
        self.emit.printout(upd + idx + addop)

        idx_update, _ = self.visit(
            ctx.name, Access(o.frame, o.sym, True, True))
        self.emit.printout(idx_update)
        self.emit.printout(self.emit.emitGOTO(start_label, o.frame))

        self.emit.printout(self.emit.emitLABEL(end_label, o.frame))
        self.emit.printout(self.emit.emitLABEL(
            o.frame.getBreakLabel(), o.frame))
        o.frame.exitLoop()

    # Done visitContinue
    def visitContinue(self, ctx, o):
        self.emit.printout(self.emit.emitGOTO(
            o.frame.getContinueLabel(), o.frame))

    # Done visitBreak
    def visitBreak(self, ctx, o):
        self.emit.printout(self.emit.emitGOTO(
            o.frame.getBreakLabel(), o.frame))

    # Done visitReturn
    def visitReturn(self, ctx: Return, o: SubBody):
        self.return_visited = True
        retType = o.frame.returnType
        if not type(retType) is VoidType:
            expCode, expType = self.visit(
                ctx.expr, Access(o.frame, o.sym, False, True))
            self.emit.printout(expCode)
        self.emit.printout(self.emit.emitRETURN(retType, o.frame))

    # Done Assign
    def visitAssign(self, ctx: Assign, o: SubBody):
        rhs_access = Access(o.frame, o.sym, False, True)
        rhs, rhs_type = self.visit(ctx.rhs, rhs_access)
        lhs_access = Access(o.frame, o.sym, True, True)
        lhs, lhs_type = self.visit(ctx.lhs, lhs_access)
        self.emit.printout(rhs)
        self.emit.printout(lhs)

    # Done visitCallStmt
    def visitCallStmt(self, ctx: CallStmt, o: SubBody):
        for env in o.sym:
            check = False
            for symbol in env:
                if ctx.name.name == symbol.name:
                    sym = symbol
                    check = False
                    break
            if check:
                break
        cname = sym.value.value
        ctype = sym.mtype

        paramsCode = ""
        for x in ctx.args:
            pCode, pType = self.visit(x, Access(o.frame, o.sym, False, True))
            paramsCode = paramsCode + pCode

        code = paramsCode + \
            self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, o.frame)
        self.emit.printout(code)

    def visitNumberLiteral(self, ctx: NumberLiteral, o):
        return self.emit.emitPUSHCONST(str(ctx.value), NumberType(), o.frame), NumberType()

    def visitBooleanLiteral(self, ctx: BooleanLiteral, o):
        return self.emit.emitPUSHCONST(ctx.value, BoolType(), o.frame), BoolType()

    def visitStringLiteral(self, ctx: StringLiteral, o):
        return self.emit.emitPUSHCONST("\"" + ctx.value + "\"", StringType(), o.frame), StringType()

    def visitArrayLiteral(self, ast, param):
        pass


class FuncZcode(Type):
    def __init__(self, param=[], typ=None, body=False):
        self.param = param
        self.typ = typ
        self.body = body


class CheckType(BaseVisitor):
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

    def visitVarDecl(self, ast: VarDecl, param):
        param[0][ast.name.name] = None
        if ast.varInit:
            typ = self.visit(ast.varInit, param)
            if type(typ) is FuncZcode:
                if ast.varType:
                    varType = self.visit(ast.varType, param)
                    self.infer(ast.varInit, varType, param)
            else:
                if ast.varType:
                    varType = self.visit(ast.varType, param)
                    if typ is None:
                        self.infer(ast.varInit, varType, param)
                    elif type(typ) is ArrayType and typ.eleType is None:
                        check = self.infer_array(ast.varInit, varType, param)
                    typ = varType
        else:
            if ast.varType:
                typ = self.visit(ast.varType, param)
            else:
                typ = None
        param[0][ast.name.name] = typ
        return typ

    def visitFuncDecl(self, ast: FuncDecl, param):
        list_param = {}
        type_param = []
        env = [list_param] + param
        for decl in ast.param:
            try:
                type_param.append(self.visit(decl, env))
            except Exception as e:
                continue

        if ast.body is None:
            self.list_functions[ast.name.name] = FuncZcode(
                type_param, None, False)
            return
        if ast.name.name in self.list_functions:
            para = self.list_functions[ast.name.name].param
            self.list_functions[ast.name.name].body = True
        self.return_visited = False
        self.visit(ast.body, env)
        if self.return_visited:
            if ast.name.name in self.list_functions:
                method = self.list_functions[ast.name.name]
                if method.typ is None and self.return_function["type"] is None:
                    pass
                elif method.typ is None:
                    self.list_functions[ast.name.name].typ = self.return_function["type"]
            else:
                self.list_functions[ast.name.name] = FuncZcode(
                    type_param, self.return_function["type"], True)
        else:
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
            return NumberType()
        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            if rtype is None:
                self.infer(ast.right, NumberType(), param)
                rtype = NumberType()
            return BoolType()
        elif ast.op in ['and', 'or']:
            if rtype is None:
                self.infer(ast.right, BoolType(), param)
                rtype = BoolType()
            return BoolType()
        elif ast.op == "==":
            if rtype is None:
                self.infer(ast.right, StringType(), param)
                rtype = StringType()
            return BoolType()
        elif ast.op == "...":
            if rtype is None:
                self.infer(ast.right, StringType(), param)
                rtype = StringType()
            return StringType()

    def visitUnaryOp(self, ast: UnaryOp, param):
        operand_type = self.visit(ast.operand, param)
        if type(operand_type) is FuncZcode:
            operand_type = operand_type.typ
        if ast.op == "-":
            if operand_type is None:
                self.infer(ast.operand, NumberType(), param)
            return NumberType()
        elif ast.op == "not":
            if operand_type is None:
                self.infer(ast.operand, NumberType(), param)
            return BoolType()

    def visitCallExpr(self, ast: CallExpr, param):
        method = self.list_functions[ast.name.name]
        for i in range(len(method.param)):
            typ = self.visit(ast.args[i], param)
            if typ is None:
                self.infer(ast.args[i], method.param[i], param)
            elif type(typ) is ArrayType and typ.eleType is None:
                check = self.infer_array(ast.args[i], method.param[i], param)
        return method.typ

    def visitId(self, ast: Id, param):
        for env in param:
            if ast.name in env:
                return env[ast.name]

    def visitArrayCell(self, ast: ArrayCell, param):
        typ = self.visit(ast.arr, param)
        if typ is None:
            pass
        else:
            for expr in ast.idx:
                typ_expr = self.visit(expr, param)
                if typ_expr is None:
                    self.infer(expr, NumberType(), param)
                    typ_expr = NumberType()
            if len(typ.size) < len(ast.idx):
                pass
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
        self.visit(ast.thenStmt, param)
        for expr, stmt in ast.elifStmt:
            typ = self.visit(expr, param)
            if typ is None:
                self.infer(ast.expr, BoolType(), param)
            self.visit(stmt, param)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)

    def visitFor(self, ast: For, param):
        id_type = self.visit(ast.name, param)
        if id_type is None:
            self.infer(ast.name, NumberType(), param)
        cond_type = self.visit(ast.condExpr, param)
        if cond_type is None:
            self.infer(ast.condExpr, BoolType(), param)
        upd_type = self.visit(ast.updExpr, param)
        if upd_type is None:
            self.infer(ast.updExpr, NumberType(), param)
        self.block_for += 1
        self.visit(ast.body, param)
        self.block_for -= 1

    def visitContinue(self, ast, param):
        pass

    def visitBreak(self, ast, param):
        pass

    def visitReturn(self, ast: Return, param):
        if not self.return_visited:
            self.return_visited = True
            if ast.expr is None:
                self.return_function = {"stmt": ast, "type": VoidType()}
            else:
                typ = self.visit(ast.expr, param)
                self.return_function = {"stmt": ast, "type": typ}
        else:
            if ast.expr is None:
                pass
            else:
                typ = self.visit(ast.expr, param)
                if typ is None:
                    self.infer(ast.expr, self.return_function["type"], param)
                elif type(typ) is ArrayType and typ.eleType is None:
                    self.infer_array(
                        ast.expr, self.return_function["type"], param)

    def visitAssign(self, ast: Assign, param):
        rtype = self.visit(ast.rhs, param)
        ltype = self.visit(ast.lhs, param)
        if ltype is None and rtype is None:
            pass
        elif ltype is None:
            self.infer(ast.lhs, rtype, param)
        elif rtype is None:
            self.infer(ast.rhs, ltype, param)
        else:
            if type(ltype) is ArrayType and type(rtype) is ArrayType:
                if ltype.eleType is None and rtype.eleType is None:
                    pass
                elif ltype.eleType is None:
                    check = self.infer_array(ast.lhs, rtype, param)
                elif rtype.eleType is None:
                    check = self.infer_array(ast.rhs, ltype, param)

    def visitCallStmt(self, ast, param):
        method = self.list_functions[ast.name.name]
        for i in range(len(method.param)):
            typ = self.visit(ast.args[i], param)
            if typ is None:
                self.infer(ast.args[i], method.param[i], param)
            elif type(typ) is ArrayType and typ.eleType is None:
                if type(method.param[i]) is not ArrayType:
                    pass
                else:
                    check = self.infer_array(
                        ast.args[i], method.param[i], param)
        if method.typ is None:
            method.typ = VoidType()
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
                if type(typ) is ArrayType:
                    return ArrayType([float(len(ast.value))] + typ.size, typ.eleType)
                else:
                    return ArrayType([float(len(ast.value))], typ)
        return ArrayType([float(len(ast.value))], None)
