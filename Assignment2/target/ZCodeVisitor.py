# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#runlist.
    def visitRunlist(self, ctx:ZCodeParser.RunlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#run.
    def visitRun(self, ctx:ZCodeParser.RunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameterlist.
    def visitParameterlist(self, ctx:ZCodeParser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameterprime.
    def visitParameterprime(self, ctx:ZCodeParser.ParameterprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newlinesep.
    def visitNewlinesep(self, ctx:ZCodeParser.NewlinesepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#endfuncdecl.
    def visitEndfuncdecl(self, ctx:ZCodeParser.EndfuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstmt.
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#eliflist.
    def visitEliflist(self, ctx:ZCodeParser.EliflistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elselist.
    def visitElselist(self, ctx:ZCodeParser.ElselistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#onlyifstmt.
    def visitOnlyifstmt(self, ctx:ZCodeParser.OnlyifstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifstmt.
    def visitElifstmt(self, ctx:ZCodeParser.ElifstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elsestmt.
    def visitElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockstmt.
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statementlist.
    def visitStatementlist(self, ctx:ZCodeParser.StatementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcstmt.
    def visitFuncstmt(self, ctx:ZCodeParser.FuncstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnstmt.
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continuestmt.
    def visitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakstmt.
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstmt.
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignstmt.
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elementarray.
    def visitElementarray(self, ctx:ZCodeParser.ElementarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardeclstmt.
    def visitVardeclstmt(self, ctx:ZCodeParser.VardeclstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newlinelist.
    def visitNewlinelist(self, ctx:ZCodeParser.NewlinelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varstartdecl.
    def visitVarstartdecl(self, ctx:ZCodeParser.VarstartdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamicstartdecl.
    def visitDynamicstartdecl(self, ctx:ZCodeParser.DynamicstartdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#normaldecl.
    def visitNormaldecl(self, ctx:ZCodeParser.NormaldeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraydecl.
    def visitArraydecl(self, ctx:ZCodeParser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funccall.
    def visitFunccall(self, ctx:ZCodeParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argumentlist.
    def visitArgumentlist(self, ctx:ZCodeParser.ArgumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argueprime.
    def visitArgueprime(self, ctx:ZCodeParser.ArgueprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arguelement.
    def visitArguelement(self, ctx:ZCodeParser.ArguelementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression1.
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression2.
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression3.
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression4.
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression5.
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression6.
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#subexpression.
    def visitSubexpression(self, ctx:ZCodeParser.SubexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#element_expression.
    def visitElement_expression(self, ctx:ZCodeParser.Element_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operator.
    def visitIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayexpression.
    def visitArrayexpression(self, ctx:ZCodeParser.ArrayexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraylit.
    def visitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sizelist.
    def visitSizelist(self, ctx:ZCodeParser.SizelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraytype.
    def visitArraytype(self, ctx:ZCodeParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#eleprime.
    def visitEleprime(self, ctx:ZCodeParser.EleprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiplyingoperator.
    def visitMultiplyingoperator(self, ctx:ZCodeParser.MultiplyingoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#addingoperator.
    def visitAddingoperator(self, ctx:ZCodeParser.AddingoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logicaloperator.
    def visitLogicaloperator(self, ctx:ZCodeParser.LogicaloperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relateoperator.
    def visitRelateoperator(self, ctx:ZCodeParser.RelateoperatorContext):
        return self.visitChildren(ctx)



del ZCodeParser