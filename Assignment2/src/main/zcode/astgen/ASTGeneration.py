# from src.main.zcode.parser.ZCodeVisitor import ZCodeVisitor
# from src.main.zcode.parser.ZCodeParser import ZCodeParser
# from src.main.zcode.utils.AST import *
from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.runlist()))

    def visitRunlist(self, ctx: ZCodeParser.RunlistContext):
        return [self.visit(ctx.run())] + self.visit(ctx.runlist()) if ctx.runlist() else [self.visit(ctx.run())]

    def visitRun(self, ctx: ZCodeParser.RunContext):
        return self.visit(ctx.funcdecl()) if ctx.funcdecl() else self.visit(ctx.vardeclstmt())

    def visitFuncdecl(self, ctx: ZCodeParser.FuncdeclContext):
        if ctx.endfuncdecl():
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.parameterlist()), self.visit(ctx.endfuncdecl()))
        else:
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.parameterlist()))

    def visitParameterlist(self, ctx: ZCodeParser.ParameterlistContext):
        return self.visit(ctx.parameterprime()) if ctx.parameterprime() else []

    def visitParameterprime(self, ctx: ZCodeParser.ParameterprimeContext):
        return [self.visit(ctx.param())] + self.visit(ctx.parameterprime()) if ctx.parameterprime() else [self.visit(ctx.param())]

    def visitParam(self, ctx: ZCodeParser.ParamContext):
        if ctx.IDENTIFIER():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ()))
        else:
            arraylit = self.visit(ctx.arraylit())
            id = arraylit["id"]
            size = arraylit["size"]
            return VarDecl(name=id, varType=ArrayType(size, self.visit(ctx.typ())))

    def visitNewlinesep(self, ctx: ZCodeParser.NewlinesepContext):
        return self.visit(ctx.newlinelist()) if ctx.newlinelist() else []

    def visitEndfuncdecl(self, ctx: ZCodeParser.EndfuncdeclContext):
        return self.visit(ctx.returnstmt()) if ctx.returnstmt() else self.visit(ctx.blockstmt())

    def visitIfstmt(self, ctx: ZCodeParser.IfstmtContext):
        onlyifstmt = self.visit(ctx.onlyifstmt())
        return If(onlyifstmt["expr"], onlyifstmt["thenStmt"], self.visit(ctx.eliflist()), self.visit(ctx.elselist()))

    def visitEliflist(self, ctx: ZCodeParser.EliflistContext):
        return [self.visit(ctx.elifstmt())] + self.visit(ctx.eliflist()) if ctx.elifstmt() else []

    def visitElselist(self, ctx: ZCodeParser.ElselistContext):
        return self.visit(ctx.elsestmt()) if ctx.elsestmt() else None

    def visitOnlyifstmt(self, ctx: ZCodeParser.OnlyifstmtContext):
        return {"expr": self.visit(ctx.expression()), "thenStmt": self.visit(ctx.statement())}

    def visitElifstmt(self, ctx: ZCodeParser.ElifstmtContext):
        return (self.visit(ctx.expression()), self.visit(ctx.statement()))

    def visitElsestmt(self, ctx: ZCodeParser.ElsestmtContext):
        return self.visit(ctx.statement())

    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitBlockstmt(self, ctx: ZCodeParser.BlockstmtContext):
        return Block(self.visit(ctx.statementlist()))

    def visitStatementlist(self, ctx: ZCodeParser.StatementlistContext):
        return [self.visit(ctx.statement())] + self.visit(ctx.statementlist()) if ctx.statement() else []

    def visitFuncstmt(self, ctx: ZCodeParser.FuncstmtContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.argumentlist()))

    def visitReturnstmt(self, ctx: ZCodeParser.ReturnstmtContext):
        return Return(self.visit(ctx.expression())) if ctx.expression() else Return()

    def visitContinuestmt(self, ctx: ZCodeParser.ContinuestmtContext):
        return Continue()

    def visitBreakstmt(self, ctx: ZCodeParser.BreakstmtContext):
        return Break()

    def visitForstmt(self, ctx: ZCodeParser.ForstmtContext):
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)), self.visit(ctx.statement()))

    def visitAssignstmt(self, ctx: ZCodeParser.AssignstmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expression()))

    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        return Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.elementarray())

    def visitElementarray(self, ctx: ZCodeParser.ElementarrayContext):
        arr = Id(ctx.IDENTIFIER().getText())
        idx = self.visit(ctx.index_operator())
        return ArrayCell(arr, idx)

    def visitVardeclstmt(self, ctx: ZCodeParser.VardeclstmtContext):
        return self.visit(ctx.vardecl())

    def visitNewlinelist(self, ctx: ZCodeParser.NewlinelistContext):
        pass

    def visitVardecl(self, ctx: ZCodeParser.VardeclContext):
        return self.visit(ctx.getChild(0))

    def visitVarstartdecl(self, ctx: ZCodeParser.VarstartdeclContext):
        return VarDecl(name=Id(ctx.IDENTIFIER().getText()), modifier=ctx.VAR().getText(), varInit=self.visit(ctx.expression()))

    def visitDynamicstartdecl(self, ctx: ZCodeParser.DynamicstartdeclContext):
        if ctx.getChildCount() == 4:
            return VarDecl(name=Id(ctx.IDENTIFIER().getText()), modifier=ctx.DYNAMIC().getText(), varInit=self.visit(ctx.expression()))
        else:
            return VarDecl(name=Id(ctx.IDENTIFIER().getText()), modifier=ctx.DYNAMIC().getText())

    def visitNormaldecl(self, ctx: ZCodeParser.NormaldeclContext):
        if ctx.getChildCount() == 4:
            return VarDecl(name=Id(ctx.IDENTIFIER().getText()), varType=self.visit(ctx.typ()), varInit=self.visit(ctx.expression()))
        else:
            return VarDecl(name=Id(ctx.IDENTIFIER().getText()), varType=self.visit(ctx.typ()))

    def visitArraydecl(self, ctx: ZCodeParser.ArraydeclContext):
        arraylit = self.visit(ctx.arraylit())
        id = arraylit["id"]
        size = arraylit["size"]
        if ctx.getChildCount() == 4:
            return VarDecl(name=id, varType=ArrayType(size, self.visit(ctx.typ())), varInit=self.visit(ctx.expression()))
        else:
            return VarDecl(name=id, varType=ArrayType(size, self.visit(ctx.typ())))

    def visitTyp(self, ctx: ZCodeParser.TypContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        else:
            return StringType()

    def visitFunccall(self, ctx: ZCodeParser.FunccallContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.argumentlist()))

    def visitArgumentlist(self, ctx: ZCodeParser.ArgumentlistContext):
        return self.visit(ctx.argueprime()) if ctx.argueprime() else []

    def visitArgueprime(self, ctx: ZCodeParser.ArgueprimeContext):
        return [self.visit(ctx.arguelement())] + self.visit(ctx.argueprime()) if ctx.argueprime() else [self.visit(ctx.arguelement())]

    def visitArguelement(self, ctx: ZCodeParser.ArguelementContext):
        return self.visit(ctx.getChild(0))

    def visitExpression(self, ctx: ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            op = ctx.STRCON().getText()
            left = self.visit(ctx.expression1(0))
            right = self.visit(ctx.expression1(1))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression1(0))

    def visitExpression1(self, ctx: ZCodeParser.Expression1Context):
        if ctx.getChildCount() == 3:
            op = self.visit(ctx.relateoperator())
            left = self.visit(ctx.expression2(0))
            right = self.visit(ctx.expression2(1))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression2(0))

    def visitExpression2(self, ctx: ZCodeParser.Expression2Context):
        if ctx.getChildCount() == 3:
            op = self.visit(ctx.logicaloperator())
            left = self.visit(ctx.expression2())
            right = self.visit(ctx.expression3())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression3())

    def visitExpression3(self, ctx: ZCodeParser.Expression3Context):
        if ctx.getChildCount() == 3:
            op = self.visit(ctx.addingoperator())
            left = self.visit(ctx.expression3())
            right = self.visit(ctx.expression4())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression4())

    def visitExpression4(self, ctx: ZCodeParser.Expression4Context):
        if ctx.getChildCount() == 3:
            op = self.visit(ctx.multiplyingoperator())
            left = self.visit(ctx.expression4())
            right = self.visit(ctx.expression5())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression5())

    def visitExpression5(self, ctx: ZCodeParser.Expression5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.NEG().getText(), self.visit(ctx.expression5()))
        else:
            return self.visit(ctx.expression6())

    def visitExpression6(self, ctx: ZCodeParser.Expression6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.expression6()))
        else:
            return self.visit(ctx.operand())

    def visitOperand(self, ctx: ZCodeParser.OperandContext):
        if ctx.NUMBERLIT():
            return NumberLiteral(float(ctx.NUMBERLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLEANLIT():
            return BooleanLiteral(True) if ctx.BOOLEANLIT().getText() == "true" else BooleanLiteral(False)
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.getChild(0))

    def visitSubexpression(self, ctx: ZCodeParser.SubexpressionContext):
        return self.visit(ctx.expression())

    def visitElement_expression(self, ctx: ZCodeParser.Element_expressionContext):
        return ArrayCell(self.visit(ctx.arrayexpression()), self.visit(ctx.index_operator()))

    def visitIndex_operator(self, ctx: ZCodeParser.Index_operatorContext):
        return [self.visit(ctx.expression())] + self.visit(ctx.index_operator()) if ctx.index_operator() else [self.visit(ctx.expression())]

    def visitArrayexpression(self, ctx: ZCodeParser.ArrayexpressionContext):
        return Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.funccall())

    def visitArraylit(self, ctx: ZCodeParser.ArraylitContext):
        return {"id": Id(ctx.IDENTIFIER().getText()), "size": self.visit(ctx.sizelist())}

    def visitSizelist(self, ctx: ZCodeParser.SizelistContext):
        return [float(ctx.NUMBERLIT().getText())] + self.visit(ctx.sizelist()) if ctx.sizelist() else [float(ctx.NUMBERLIT().getText())]

    def visitArraytype(self, ctx: ZCodeParser.ArraytypeContext):
        return ArrayLiteral(self.visit(ctx.eleprime()))

    def visitEleprime(self, ctx: ZCodeParser.EleprimeContext):
        return [self.visit(ctx.expression())] + self.visit(ctx.eleprime()) if ctx.eleprime() else [self.visit(ctx.expression())]

    def visitMultiplyingoperator(self, ctx: ZCodeParser.MultiplyingoperatorContext):
        return ctx.getChild(0).getText()

    def visitAddingoperator(self, ctx: ZCodeParser.AddingoperatorContext):
        return ctx.getChild(0).getText()

    def visitLogicaloperator(self, ctx: ZCodeParser.LogicaloperatorContext):
        return ctx.getChild(0).getText()

    def visitRelateoperator(self, ctx: ZCodeParser.RelateoperatorContext):
        return ctx.getChild(0).getText()
