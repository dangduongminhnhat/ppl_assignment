import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_301(self):
        input = """
            number MiNhat
        """
        expect = str(Program([
            VarDecl(Id("MiNhat"), NumberType())
        ]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = """
            string MiNhat <- 1
        """
        expect = str(Program([
            VarDecl(Id("MiNhat"), StringType(), None, NumberLiteral(1.0))
        ]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = """
            string MiNhat
            bool MiNhat
            string MiNhat <- 1
            bool MiNhat <- 1
        """
        expect = str(Program([
            VarDecl(Id("MiNhat"), StringType()),
            VarDecl(Id("MiNhat"), BoolType()),
            VarDecl(Id("MiNhat"), StringType(), None, NumberLiteral(1.0)),
            VarDecl(Id("MiNhat"), BoolType(), None, NumberLiteral(1.0))
        ]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = """
            string MiNhat[5] <- 1
            string MiNhat[5]
        """
        expect = str(Program([
            VarDecl(Id("MiNhat"), ArrayType(
                [5.0], StringType()), None, NumberLiteral(1.0)),
            VarDecl(Id("MiNhat"), ArrayType([5.0], StringType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """
            number MiNhat[5,3,4.2] <- 1
            bool MiNhat[2,3,4]
        """
        expect = str(Program([
            VarDecl(Id("MiNhat"), ArrayType(
                [5.0, 3.0, 4.2], NumberType()), None, NumberLiteral(1.0)),
            VarDecl(Id("MiNhat"), ArrayType([2.0, 3.0, 4.0], BoolType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """
            dynamic MiNhat <- 1
            dynamic MiNhat
        """
        expect = str(Program([
            VarDecl(Id("MiNhat"), None, "dynamic", NumberLiteral(1.0)),
            VarDecl(Id("MiNhat"), None, "dynamic")
        ]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """
            var MiNhat <- 1
        """
        expect = str(Program([
            VarDecl(Id("MiNhat"), None, "var", NumberLiteral(1.0))
        ]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = """
            func main()
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], None)
        ]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = """
            func main()
                begin
                end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = """
            func main()
                begin
                break
                end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                Break()]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number MiNhat[1,2])
                return
        """
        expect = str(Program([
            FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
            FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()),
                                  VarDecl(Id("a"), StringType()),
                                  VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
            FuncDecl(Id("main"), [VarDecl(Id("MiNhat"), ArrayType(
                [1.0, 2.0], NumberType()))], Return(None))
        ]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """
            var x <- 1
            var x <- "123"
            var x <- true
            var x <- false
        """
        expect = str(Program([
            VarDecl(Id("x"), None, "var",  NumberLiteral(1.0)),
            VarDecl(Id("x"), None, "var",  StringLiteral("123")),
            VarDecl(Id("x"), None, "var",  BooleanLiteral(True)),
            VarDecl(Id("x"), None, "var",  BooleanLiteral(False))
        ]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """
            var x <- [1, "a", true, false]
        """
        expect = str(Program([
            VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(
                1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """
            var x <- [[1], [1]]
            var x <- [[1]]
        """
        expect = str(Program([
            VarDecl(Id("x"), None, "var",  ArrayLiteral(
                [ArrayLiteral([NumberLiteral(1.0)]), ArrayLiteral([NumberLiteral(1.0)])])),
            VarDecl(Id("x"), None, "var",  ArrayLiteral(
                [ArrayLiteral([NumberLiteral(1.0)])]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """
            var x <- 1 ... "2"
            var x <- 1 <= "2"
            var x <- 1 and 2 or 3
            var x <- 1 + 2 - 3
            var x <- 1 * 2 / 3 % 4
            var x <- ---1
            var x <- not not 1
            var x <- x
            var x <- a[1,2,3]
        """
        expect = str(Program([
            VarDecl(Id("x"), None, "var",  BinaryOp(
                "...", NumberLiteral(1.0), StringLiteral("2"))),
            VarDecl(Id("x"), None, "var",  BinaryOp(
                "<=", NumberLiteral(1.0), StringLiteral("2"))),
            VarDecl(Id("x"), None, "var",  BinaryOp("or", BinaryOp(
                "and", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
            VarDecl(Id("x"), None, "var",  BinaryOp(
                "-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
            VarDecl(Id("x"), None, "var",  BinaryOp("%", BinaryOp(
                "/", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0))),
            VarDecl(Id("x"), None, "var",  UnaryOp(
                "-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0))))),
            VarDecl(Id("x"), None, "var",  UnaryOp(
                "not", UnaryOp("not", NumberLiteral(1.0)))),
            VarDecl(Id("x"), None, "var",  Id("x")),
            VarDecl(Id("x"), None, "var",  ArrayCell(
                Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """
            var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
        """
        expect = str(Program([
            VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(4.0), BinaryOp(
                "+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", Id("a"), NumberLiteral(3.0))), Id("c")), UnaryOp("-", NumberLiteral(1.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(2.0)))))))
        ]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = """
            var x <- -a[1+2] ... 2
        """
        expect = str(Program([
            VarDecl(Id("x"), None, "var",  BinaryOp("...", UnaryOp("-", ArrayCell(Id("a"),
                    [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])), NumberLiteral(2.0)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """
            var x <- fun()
        """
        expect = str(Program([
            VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), []))
        ]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """
            var x <- fun(1+1, "a")
        """
        expect = str(Program([
            VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [BinaryOp(
                "+", NumberLiteral(1.0), NumberLiteral(1.0)), StringLiteral("a")]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """
            var x <- fun(fun())
        """
        expect = str(Program([
            VarDecl(Id("x"), None, "var",  CallExpr(
                Id("fun"), [CallExpr(Id("fun"), [])]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """
            var x <- (2 ... 3) ... 4
        """
        expect = str(Program([
            VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp(
                "...", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(4.0)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """
            func main()
                begin
                    continue
                end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                Continue()]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """
            func main()
                begin
                    continue
                    continue
                    break
                    begin
                        continue
                        continue
                        break                    
                    end
                end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                Continue(),
                Continue(),
                Break(),
                Block([
                    Continue(),
                    Continue(),
                    Break()])]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = """
            func main()
                begin
                    return  1 + 1
                    return
                end
            func main()
                return 1
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0))),
                Return()])),
            FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """
            func main()
                begin
                    main(a)
                    main(1,1)
                end
            func main()
                begin
                main()
                end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("main"), [Id("a")]),
                CallStmt(Id("main"), [NumberLiteral(1.0), NumberLiteral(1.0)])])),
            FuncDecl(Id("main"), [], Block([
                CallStmt(Id("main"), [])]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input = """
            func main()
                begin
                    a <- 1
                    a[1] <- 2
                    a[3,2] <- 4 + 2
                end
            func main()
                begin
                a[1+1, 3] <- 1
                end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                Assign(Id("a"), NumberLiteral(1.0)),
                Assign(
                    ArrayCell(Id("a"), [NumberLiteral(1.0)]), NumberLiteral(2.0)),
                Assign(ArrayCell(Id("a"), [NumberLiteral(3.0), NumberLiteral(2.0)]), BinaryOp("+", NumberLiteral(4.0), NumberLiteral(2.0)))])),
            FuncDecl(Id("main"), [], Block([
                Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), NumberLiteral(3.0)]), NumberLiteral(1.0))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = """
            func main()
                begin
                    for i until i > 2 by 1 + 1
                        print(1)
                end
            func main()
                begin
                    for i until i by [1]
                    begin
                        print(1)
                    end
                end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(2.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), CallStmt(Id("print"), [NumberLiteral(1.0)]))])),
            FuncDecl(Id("main"), [], Block([
                For(Id("i"), Id("i"), ArrayLiteral([NumberLiteral(1.0)]), Block([
                    CallStmt(Id("print"), [NumberLiteral(1.0)])]))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = """
            func main()
                begin
                    if (true) return 1
                end
            func main()
                begin
                    if (true) return 2
                    else return 3
                end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], None)])),
            FuncDecl(Id("main"), [], Block([
                If(BooleanLiteral(True), Return(NumberLiteral(2.0)), [], Return(NumberLiteral(3.0)))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input = """
            func main()
                begin
                    if (true) return 1
                    elif (true) return 1
                    elif (true) return 1
                    else return 1
                end

        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                If(BooleanLiteral(True), Return(NumberLiteral(1.0)),
                   [(BooleanLiteral(True), Return(NumberLiteral(1.0))),
                    (BooleanLiteral(True), Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = """
            var c <- a[1,2]
            var c <- fun()[1,2]
            var c <- fun(1,2)[1,3]
        """
        expect = str(Program([
            VarDecl(Id("c"), None, "var", ArrayCell(
                Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("c"), None, "var", ArrayCell(
                CallExpr(Id("fun"), []), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("fun"), [NumberLiteral(
                1.0), NumberLiteral(2.0)]), [NumberLiteral(1.0), NumberLiteral(3.0)]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input = """
            func main()
            begin
                var c <- 2e5
                dynamic c <- 2.56
                dynamic c
                number c[2e2, 2] <- 3.6
                string c[3.823]
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block(
                [VarDecl(Id("c"), None, "var", NumberLiteral(200000.0)),
                 VarDecl(Id("c"), None, "dynamic", NumberLiteral(2.56)),
                 VarDecl(Id("c"), None, "dynamic"),
                 VarDecl(Id("c"), ArrayType(
                     [200.0, 2.0], NumberType()), None, NumberLiteral(3.6)),
                 VarDecl(Id("c"), ArrayType([3.823], StringType()), None)
                 ]))]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        else return 1
                end

        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True),
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(1.0))), [], None)
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        else return 1
                    else return 1
                end

        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True),
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)),
                  [], Return(NumberLiteral(1.0))),
               [], Return(NumberLiteral(1.0)))
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 1
                        else return 1
                end

        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True),
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True), Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0))), [], None)
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 1
                        elif (true) return 1
                end

        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True),
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True), Return(NumberLiteral(1.0))), (BooleanLiteral(True), Return(NumberLiteral(1.0)))]), [], None)
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 1
                        elif (true) return 1
                        else return 1
                    elif (true) return 1
                    elif (true) return 1                        
                    else return 1
                end

        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True),
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True), Return(NumberLiteral(1.0))), (BooleanLiteral(True), Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0))), [(BooleanLiteral(True), Return(NumberLiteral(1.0))), (BooleanLiteral(True), Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input = """
## print array recursively
func printArr(number a[100], number length)
begin
    if (length < 0)
        return
    printArr(a, length - 1)
    writeNumber(a[length - 1])
    writeString(" ")
end
"""
        expect = "Program([FuncDecl(Id(printArr), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([If((BinaryOp(<, Id(length), NumLit(0.0)), Return()), [], None), CallStmt(Id(printArr), [Id(a), BinaryOp(-, Id(length), NumLit(1.0))]), CallStmt(Id(writeNumber), [ArrayCell(Id(a), [BinaryOp(-, Id(length), NumLit(1.0))])]), CallStmt(Id(writeString), [StringLit( )])]))])"
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input = """
func main ()
begin
    if (1)
        b()
    elif (2)
        if (3)
            c()
        elif (4)
            d()
        else
            e()
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(b), [])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(c), [])), [(NumLit(4.0), CallStmt(Id(d), []))], CallStmt(Id(e), [])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input = """
string s <- a ... b
"""
        expect = """Program([VarDecl(Id(s), StringType, None, BinaryOp(..., Id(a), Id(b)))])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = """
func a()
begin
    begin
        begin
            begin
                begin
                    begin
                        begin
                        call()
                            begin
                                ##aaaa
                                call()
                                call()
                            end
                        end
                    end
                end
            end
        end
    end
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([Block([Block([Block([Block([Block([Block([CallStmt(Id(call), []), Block([CallStmt(Id(call), []), CallStmt(Id(call), [])])])])])])])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        input = """
func abc(number _a, string a0, number b[1, 2, 0])
begin
    if (a > b) number c
    elif (  a > b) number c
    if (a > b   ) number c
    elif ( a > b ) number c
    else number c
    if (     a > b ) number c
    else number c
    return c
end
"""
        expect = """Program([FuncDecl(Id(abc), [VarDecl(Id(_a), NumberType, None, None), VarDecl(Id(a0), StringType, None, None), VarDecl(Id(b), ArrayType([1.0, 2.0, 0.0], NumberType), None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], None), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None)), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None)), Return(Id(c))]))])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
        input = """
## this is pre-declaration func
func main()


## this is function definition
func main()     begin
    number a <- 1.2e-12
    number c <- (b + a) / c * a - d + goo()[1, 2, 3] * goo(a + b) * a[1, foo(), _c]
    foo()
    number k <- goo()[a + b, foo(), 1e-1]
    return a
end
"""
        expect = """Program([FuncDecl(Id(main), [], None), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(1.2e-12)), VarDecl(Id(c), NumberType, None, BinaryOp(+, BinaryOp(-, BinaryOp(*, BinaryOp(/, BinaryOp(+, Id(b), Id(a)), Id(c)), Id(a)), Id(d)), BinaryOp(*, BinaryOp(*, ArrayCell(CallExpr(Id(goo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), CallExpr(Id(goo), [BinaryOp(+, Id(a), Id(b))])), ArrayCell(Id(a), [NumLit(1.0), CallExpr(Id(foo), []), Id(_c)])))), CallStmt(Id(foo), []), VarDecl(Id(k), NumberType, None, ArrayCell(CallExpr(Id(goo), []), [BinaryOp(+, Id(a), Id(b)), CallExpr(Id(foo), []), NumLit(0.1)])), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
        input = """
## this is a comment




## this is a comment
    ## this is a comment
func test_comment() ##this is no space comment
begin
    number a ## this is allowed
    return false
end
"""
        expect = """Program([FuncDecl(Id(test_comment), [], Block([VarDecl(Id(a), NumberType, None, None), Return(BooleanLit(False))]))])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
        input = """
func test_looping(string a[1, 2], number __[0], bool cc_c)
begin
    if (a > b)
        for a until a + 1 by b + 1 if (a > b)
                if (a > b) number c
                elif (a > b) number c
                elif (a > b) number c
                else number c
            else
                break
    else
        for a until a > b by a * b / c
            for a until ssss[1, 2] by foo("hey", true, false, 1.e-3)
                if (a > b) number c
                else number c
end
"""
        expect = """Program([FuncDecl(Id(test_looping), [VarDecl(Id(a), ArrayType([1.0, 2.0], StringType), None, None), VarDecl(Id(__), ArrayType([0.0], NumberType), None, None), VarDecl(Id(cc_c), BoolType, None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), For(Id(a), BinaryOp(+, Id(a), NumLit(1.0)), BinaryOp(+, Id(b), NumLit(1.0)), If((BinaryOp(>, Id(a), Id(b)), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), (BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None))), [], Break))), [], For(Id(a), BinaryOp(>, Id(a), Id(b)), BinaryOp(/, BinaryOp(*, Id(a), Id(b)), Id(c)), For(Id(a), ArrayCell(Id(ssss), [NumLit(1.0), NumLit(2.0)]), CallExpr(Id(foo), [StringLit(hey), BooleanLit(True), BooleanLit(False), NumLit(0.001)]), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input = """
func main(number a, number b) begin
number a[1, 2] <- [[2, 3]]
string b <- 1.e-12
bool c <- "abc"
return main(a, 3, d, b)
end
"""
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([VarDecl(Id(a), ArrayType([1.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)))), VarDecl(Id(b), StringType, None, NumLit(1e-12)), VarDecl(Id(c), BoolType, None, StringLit(abc)), Return(CallExpr(Id(main), [Id(a), NumLit(3.0), Id(d), Id(b)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input = """
func test_if(string a[1, 2, 3])
begin
    if (a < b)
    if (a < b) number c
    elif (a < c)
    if (a < b) if (a < b) number c
    else number c
    if (a < b)
    if (a < b) if (a < b)
        number c
    else number c
    if (a < b) number c
    elif (a < b) number c
    else number c
end
"""
        expect = """Program([FuncDecl(Id(test_if), [VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], StringType), None, None)], Block([If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(<, Id(a), Id(c)), If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None))), [], None))], None)), [], None), If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None))), [], None)), [], None), If((BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(<, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None))]))])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        input = """
func test_exp()
begin
    bool a <- not not a and b or not not c or d or e and b < not not not c and d or e or not not e
    return a
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), BoolType, None, BinaryOp(<, BinaryOp(and, BinaryOp(or, BinaryOp(or, BinaryOp(or, BinaryOp(and, UnaryOp(not, UnaryOp(not, Id(a))), Id(b)), UnaryOp(not, UnaryOp(not, Id(c)))), Id(d)), Id(e)), Id(b)), BinaryOp(or, BinaryOp(or, BinaryOp(and, UnaryOp(not, UnaryOp(not, UnaryOp(not, Id(c)))), Id(d)), Id(e)), UnaryOp(not, UnaryOp(not, Id(e)))))), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        input = """
func test_exp()
begin
    bool a <- a <= (b = ((k > (h == (b < c))) < (d > (e == f))))
    return a
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), BoolType, None, BinaryOp(<=, Id(a), BinaryOp(=, Id(b), BinaryOp(<, BinaryOp(>, Id(k), BinaryOp(==, Id(h), BinaryOp(<, Id(b), Id(c)))), BinaryOp(>, Id(d), BinaryOp(==, Id(e), Id(f))))))), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        input = """
func test_exp()
begin
    number a <- a[1, [1, 2]]
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(a), [NumLit(1.0), ArrayLit(NumLit(1.0), NumLit(2.0))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
        input = """
func test_exp()
begin
    number a <- c[1, d[1, 2, 3, foo()[1, 2]], goo() + 1 * 3 / b, h[1, 1]]
    return a
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(c), [NumLit(1.0), ArrayCell(Id(d), [NumLit(1.0), NumLit(2.0), NumLit(3.0), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0)])]), BinaryOp(+, CallExpr(Id(goo), []), BinaryOp(/, BinaryOp(*, NumLit(1.0), NumLit(3.0)), Id(b))), ArrayCell(Id(h), [NumLit(1.0), NumLit(1.0)])])), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
        input = """
func test_exp()
begin
    number a <- [1, [1], [[1]], [[[1]]], [[[[1]]]]]
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(1.0), ArrayLit(NumLit(1.0)), ArrayLit(ArrayLit(NumLit(1.0))), ArrayLit(ArrayLit(ArrayLit(NumLit(1.0)))), ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0)))))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input = """
func foo123478_main_09()
begin
    number a <- [1, 2, [1, 2, [1, 4]], [3, 4]]
end
"""
        expect = """Program([FuncDecl(Id(foo123478_main_09), [], Block([VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(1.0), NumLit(2.0), ArrayLit(NumLit(1.0), NumLit(2.0), ArrayLit(NumLit(1.0), NumLit(4.0))), ArrayLit(NumLit(3.0), NumLit(4.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input = """
func callingDestroyer()
begin
    call()
    call(call())
    call(call(call()))
    call(call(call(call())))
    call(call(call(call(call()))))
    call(call(call(call(call(call())))))
    call(call(call(call(call(call(call()))))))
    call(call(call(call(call(call(call(call())))))))
    call(call(call(call(call(call(call(call(call()))))))))
    call(call(call(call(call(call(call(call(call(call())))))))))
    call(call(call(call(call(call(call(call(call(call(call()))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call())))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call()))))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call(call())))))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call(call(call()))))))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call(call(call(call())))))))))))))))
end
"""
        expect = """Program([FuncDecl(Id(callingDestroyer), [], Block([CallStmt(Id(call), []), CallStmt(Id(call), [CallExpr(Id(call), [])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])])])])])]), CallStmt(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [CallExpr(Id(call), [])])])])])])])])])])])])])])])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = """
func subDestroyer()
begin
    number a <- (b)
    number a <- ((b))
    number a <- (((b)))
    number a <- ((((b))))
    number a <- (((((b)))))
    number a <- ((((((b))))))
    number a <- (((((((b)))))))
    number a <- ((((((((b))))))))
    number a <- (((((((((b)))))))))
    number a <- ((((((((((b))))))))))
    number a <- (((((((((((b)))))))))))
    number a <- ((((((((((((b))))))))))))
    number a <- (((((((((((((b)))))))))))))
    number a <- ((((((((((((((b))))))))))))))
    number a <- (((((((((((((((b)))))))))))))))
end
"""
        expect = """Program([FuncDecl(Id(subDestroyer), [], Block([VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b)), VarDecl(Id(a), NumberType, None, Id(b))]))])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
        input = """
func arrayDestroyer()
begin
    number a <- [[[[[[[[[[[[[[[[[[[[[[[[[[foo()[1, 2, 3]]]]]]]]]]]]]]]]]]]]]]]]]]]
end
"""
        expect = """Program([FuncDecl(Id(arrayDestroyer), [], Block([VarDecl(Id(a), NumberType, None, ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]))))))))))))))))))))))))))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
        input = """
func unaryDestroyer()
begin
    a <- not not not---(not-(not-(not not-(not not not-(not not not not----(not-----(not not---(not not not--(foo()[0])))))))))
end
"""
        expect = """Program([FuncDecl(Id(unaryDestroyer), [], Block([AssignStmt(Id(a), UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(not, UnaryOp(-, UnaryOp(not, UnaryOp(-, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, ArrayCell(CallExpr(Id(foo), []), [NumLit(0.0)])))))))))))))))))))))))))))))))))))))))))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input = """
func main()
begin
    number x <- [foo(), foo()[1, 2, 3], x[0, 1], 12 > 3]
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, ArrayLit(CallExpr(Id(foo), []), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), ArrayCell(Id(x), [NumLit(0.0), NumLit(1.0)]), BinaryOp(>, NumLit(12.0), NumLit(3.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = """
func main(number a, string s, bool _, number xxx[1, 2, 3])
begin
    do_something(a, s, _, xxx)
end
"""
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(s), StringType, None, None), VarDecl(Id(_), BoolType, None, None), VarDecl(Id(xxx), ArrayType([1.0, 2.0, 3.0], NumberType), None, None)], Block([CallStmt(Id(do_something), [Id(a), Id(s), Id(_), Id(xxx)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input = """
func __aaa__()
begin
    number arr[0, 0, 0] <- [[1, 2, 3], ["a" ... "b", foo()["index"]], [(a and not c) = d]]
end
"""
        expect = """Program([FuncDecl(Id(__aaa__), [], Block([VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(..., StringLit(a), StringLit(b)), ArrayCell(CallExpr(Id(foo), []), [StringLit(index)])), ArrayLit(BinaryOp(=, BinaryOp(and, Id(a), UnaryOp(not, Id(c))), Id(d)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
        input = """
func calc()
begin
    number a <- 5 ## This is a
    number b <- 5 ## This is b
    number c <- 5 ## This is c
    number d <- 5 ## This is d
    ## This is e number e <- a + b + c + d
    number e <- (a) + (b) + ((c) + (d))
    return e ## This is return
end ## This is end of function
"""
        expect = """Program([FuncDecl(Id(calc), [], Block([VarDecl(Id(a), NumberType, None, NumLit(5.0)), VarDecl(Id(b), NumberType, None, NumLit(5.0)), VarDecl(Id(c), NumberType, None, NumLit(5.0)), VarDecl(Id(d), NumberType, None, NumLit(5.0)), VarDecl(Id(e), NumberType, None, BinaryOp(+, BinaryOp(+, Id(a), Id(b)), BinaryOp(+, Id(c), Id(d)))), Return(Id(e))]))])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = """
## This is a comment
 ## This is a comment
  ## This is a comment
   ## This is a comment
    ## This is a comment
     ## This is a comment
      ## This is a comment
       ## This is a comment
        ## This is a comment
         ## This is a comment


func main()
begin
    if (not not not (a and b or c and not d)) if (not not not (a and b or c and not d))
    if (not not not (a and b or c and d))
    if (not not not (a and b or c > d))
    if (foo()[1, 0])
    if ("string") if ([1, 2, 3, 4])
    if ((("a" ... "b") ... c) > ((a * b * d + foo()[1, 2, 3]) <= (not a and not not c)))
    if ((("a" ... "b") ... c) > ((a * b * d + foo()[1, 2, 3]) <= (not a and not not c)))
    if ((foo() + _() - __(12, 3, "abc", [1, 2, 3])) > __aaa__("a", "", "\\n", abc, not false, true))
    if (true) if (false) do_something()
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((UnaryOp(not, UnaryOp(not, UnaryOp(not, BinaryOp(and, BinaryOp(or, BinaryOp(and, Id(a), Id(b)), Id(c)), UnaryOp(not, Id(d)))))), If((UnaryOp(not, UnaryOp(not, UnaryOp(not, BinaryOp(and, BinaryOp(or, BinaryOp(and, Id(a), Id(b)), Id(c)), UnaryOp(not, Id(d)))))), If((UnaryOp(not, UnaryOp(not, UnaryOp(not, BinaryOp(and, BinaryOp(or, BinaryOp(and, Id(a), Id(b)), Id(c)), Id(d))))), If((UnaryOp(not, UnaryOp(not, UnaryOp(not, BinaryOp(>, BinaryOp(or, BinaryOp(and, Id(a), Id(b)), Id(c)), Id(d))))), If((ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(0.0)]), If((StringLit(string), If((ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), If((BinaryOp(>, BinaryOp(..., BinaryOp(..., StringLit(a), StringLit(b)), Id(c)), BinaryOp(<=, BinaryOp(+, BinaryOp(*, BinaryOp(*, Id(a), Id(b)), Id(d)), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])), BinaryOp(and, UnaryOp(not, Id(a)), UnaryOp(not, UnaryOp(not, Id(c)))))), If((BinaryOp(>, BinaryOp(..., BinaryOp(..., StringLit(a), StringLit(b)), Id(c)), BinaryOp(<=, BinaryOp(+, BinaryOp(*, BinaryOp(*, Id(a), Id(b)), Id(d)), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])), BinaryOp(and, UnaryOp(not, Id(a)), UnaryOp(not, UnaryOp(not, Id(c)))))), If((BinaryOp(>, BinaryOp(-, BinaryOp(+, CallExpr(Id(foo), []), CallExpr(Id(_), [])), CallExpr(Id(__), [NumLit(12.0), NumLit(3.0), StringLit(abc), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))])), CallExpr(Id(__aaa__), [StringLit(a), StringLit(), StringLit(\\n), Id(abc), UnaryOp(not, BooleanLit(False)), BooleanLit(True)])), If((BooleanLit(True), If((BooleanLit(False), CallStmt(Id(do_something), [])), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = """
func main()
begin
    number i0
    number i1
    number i2
    number i3
    number i4
    number i5
    number i6
    number i7
    for i0 until true by 1
        for i1 until false by _ * _
            for i2 until ("a" ... "c") > (not b and c or d) by 12.12e-12
                for i3 until b >= (c + foo()[1, 2]) by foo("abc", d, true)
                    for i4 until -3 or -x by "string"
                        for i5 until "" by [1, 2, 3]
                            for i6 until [[foo()[0, 0]]] by 12.e-2
                                for i7 until false by _(_,_,_)
                                    do_something()
    return
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i0), NumberType, None, None), VarDecl(Id(i1), NumberType, None, None), VarDecl(Id(i2), NumberType, None, None), VarDecl(Id(i3), NumberType, None, None), VarDecl(Id(i4), NumberType, None, None), VarDecl(Id(i5), NumberType, None, None), VarDecl(Id(i6), NumberType, None, None), VarDecl(Id(i7), NumberType, None, None), For(Id(i0), BooleanLit(True), NumLit(1.0), For(Id(i1), BooleanLit(False), BinaryOp(*, Id(_), Id(_)), For(Id(i2), BinaryOp(>, BinaryOp(..., StringLit(a), StringLit(c)), BinaryOp(or, BinaryOp(and, UnaryOp(not, Id(b)), Id(c)), Id(d))), NumLit(1.212e-11), For(Id(i3), BinaryOp(>=, Id(b), BinaryOp(+, Id(c), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(2.0)]))), CallExpr(Id(foo), [StringLit(abc), Id(d), BooleanLit(True)]), For(Id(i4), BinaryOp(or, UnaryOp(-, NumLit(3.0)), UnaryOp(-, Id(x))), StringLit(string), For(Id(i5), StringLit(), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), For(Id(i6), ArrayLit(ArrayLit(ArrayCell(CallExpr(Id(foo), []), [NumLit(0.0), NumLit(0.0)]))), NumLit(0.12), For(Id(i7), BooleanLit(False), CallExpr(Id(_), [Id(_), Id(_), Id(_)]), CallStmt(Id(do_something), []))))))))), Return()]))])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """
number arr[0, 0, 0] <- [1, 2, 3]
string arr[0, 0, 0] <- ["a", "b", "c"]
bool arr[0, 0, 0] <- [true, true, false]
func main()
begin
    number x <- arr[0, 0]
    return[1, 2, 3]
    return-3
    return"abc"
    return"abc\\t\\n\\b\\f\\r\\\\\\''""
end
"""
        expect = """Program([VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], StringType), None, ArrayLit(StringLit(a), StringLit(b), StringLit(c))), VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], BoolType), None, ArrayLit(BooleanLit(True), BooleanLit(True), BooleanLit(False))), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, ArrayCell(Id(arr), [NumLit(0.0), NumLit(0.0)])), Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), Return(UnaryOp(-, NumLit(3.0))), Return(StringLit(abc)), Return(StringLit(abc\\t\\n\\b\\f\\r\\\\\\''"))]))])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = """
func foo(number a, string s)
func main(bool arr)
func goo(number ABDS__)
func build(number ABC1092__ADBsdlhs__)
func create(number dosomething)
func hey(string arr[1, 2, 3])
func go(string arr[3, 4, 5])
func do()
func ____()
func _____abc____ABC___()
func ODLLAHJLBOSE()
func xxxxxxxxxxxxx()
"""
        expect = """Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(s), StringType, None, None)], None), FuncDecl(Id(main), [VarDecl(Id(arr), BoolType, None, None)], None), FuncDecl(Id(goo), [VarDecl(Id(ABDS__), NumberType, None, None)], None), FuncDecl(Id(build), [VarDecl(Id(ABC1092__ADBsdlhs__), NumberType, None, None)], None), FuncDecl(Id(create), [VarDecl(Id(dosomething), NumberType, None, None)], None), FuncDecl(Id(hey), [VarDecl(Id(arr), ArrayType([1.0, 2.0, 3.0], StringType), None, None)], None), FuncDecl(Id(go), [VarDecl(Id(arr), ArrayType([3.0, 4.0, 5.0], StringType), None, None)], None), FuncDecl(Id(do), [], None), FuncDecl(Id(____), [], None), FuncDecl(Id(_____abc____ABC___), [], None), FuncDecl(Id(ODLLAHJLBOSE), [], None), FuncDecl(Id(xxxxxxxxxxxxx), [], None)])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = """
func main()
begin
    number a <- 5
    begin
        number b <- 5
        begin
            number c <- 5
            begin
                number d <- a + (b) + (c) + d
                return d
            end
        end
    end
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(5.0)), Block([VarDecl(Id(b), NumberType, None, NumLit(5.0)), Block([VarDecl(Id(c), NumberType, None, NumLit(5.0)), Block([VarDecl(Id(d), NumberType, None, BinaryOp(+, BinaryOp(+, BinaryOp(+, Id(a), Id(b)), Id(c)), Id(d))), Return(Id(d))])])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input = """
func main()
begin 
    hello()
    kkap(kk(yeah(ha(idk(2,4,[2,4,[[[[[[[[[[[2]]]]]]]]]]],45],4)))))
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(hello), []), CallStmt(Id(kkap), [CallExpr(Id(kk), [CallExpr(Id(yeah), [CallExpr(Id(ha), [CallExpr(Id(idk), [NumLit(2.0), NumLit(4.0), ArrayLit(NumLit(2.0), NumLit(4.0), ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(2.0)))))))))))), NumLit(45.0)), NumLit(4.0)])])])])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
        input = """
func a() 
begin
    if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (a) return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(a), Return()), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input = """
func a() 
begin
    if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (i) return
    elif (b) if (c) return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(i), Return()), [(Id(b), If((Id(c), Return()), [], None))], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = """
func a() 
begin
    if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (i) return
    elif (b) return
    elif (c) return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(i), Return()), [(Id(b), Return()), (Id(c), Return())], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = """
func a() 
begin
    if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (i) return
    elif (b) if (c) return
    var x <-  2
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(i), Return()), [(Id(b), If((Id(c), Return()), [], None))], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None), VarDecl(Id(x), None, var, NumLit(2.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = """
func a() 
begin
    if (d) if (b) d()
    else return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = """
func a() 
begin
    if (d) if (b) d()
    else return
    else return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], Return())]))])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = """
func a() 
begin
    if (d) if (b) if(g) d()
    else return
    else return
    elif (j) return 2
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), If((Id(g), CallStmt(Id(d), [])), [], Return())), [], Return())), [(Id(j), Return(NumLit(2.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = """
func a() 
begin
    if (d) if (b) d()
    else return
    else return
    if (tiep) ha()
    elif (dung) ha()
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], Return()), If((Id(tiep), CallStmt(Id(ha), [])), [(Id(dung), CallStmt(Id(ha), []))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = """
func a() 
begin
    for doo until (doo <= 2) by "hello"...l
        exe()
    exe()
    exe()
    exe()
    exe()
    exe()
    exe()
    exe()
    exe()
    if  (a) 
    if (b) return
    elif (c) return
    else return
    else return
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello), Id(l)), CallStmt(Id(exe), [])), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), If((Id(a), If((Id(b), Return()), [(Id(c), Return())], Return())), [], Return())]))])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = """
func a() 
begin
    for doo until (doo <= 2) by "hello'""...l
        for doo until (doo <= 2) by "hello'""...l
            for doo until (doo <= 2) by "hello'""...l
                if (a) 
                    for doo until (doo <= 2) by "hello'""...l
                        return
                elif (b) 
                    for doo until (doo <= 2) by "hello'""...l
                        return
                else no()
end
"""
        expect = """Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), If((Id(a), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), Return())), [(Id(b), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), Return()))], CallStmt(Id(no), [])))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = """
func __aaa__()
begin
    number arr[0, 0, 0] <- [[1, 2, 3], ["a\\'" ... "b\\'", foo()["index\\\\"]], [(a and not c) = d]]
end
"""
        expect = """Program([FuncDecl(Id(__aaa__), [], Block([VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(..., StringLit(a\\'), StringLit(b\\')), ArrayCell(CallExpr(Id(foo), []), [StringLit(index\\\\)])), ArrayLit(BinaryOp(=, BinaryOp(and, Id(a), UnaryOp(not, Id(c))), Id(d)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = """
func qq(number bbb, number qqq, string a)	
begin
    if(a) return
    elif(b) if (c) if (d) call() 
    else return
    else return
    elif (c) call()
end
"""
        expect = """Program([FuncDecl(Id(qq), [VarDecl(Id(bbb), NumberType, None, None), VarDecl(Id(qqq), NumberType, None, None), VarDecl(Id(a), StringType, None, None)], Block([If((Id(a), Return()), [(Id(b), If((Id(c), If((Id(d), CallStmt(Id(call), [])), [], Return())), [], Return())), (Id(c), CallStmt(Id(call), []))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = """
number LOOP_COUNT <- 0
func toAsciiCode(string s)
begin 
string ascii[96] <- [" ","!","'"","#","$","%","&","\\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~",""]
number i<-0
for i until s == ascii[i] by 1
    i<-i+1
return i+32
end

func doNoThing(number n) return n
func main() begin
    number i<-0
    if (toAsciiCode("a") % 3 = 0)
        if (toAssciiCode("b") = doNoThing(toAsciiCode("b")/3)*3)
            for i until i<=doNoThing(3) by 1 LOOP_COUNT<- LOOP_COUNT ----1
        elif (toAsciiCode("c")=i) 
            if (i*i*i%128 = toAsciiCode("H"))
            for i until i<=doNoThing(100) by 1 
                if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                else for i until i<=doNoThing(100) by 1 
                    if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                    else i<-1--i 
end
"""
        expect = """Program([VarDecl(Id(LOOP_COUNT), NumberType, None, NumLit(0.0)), FuncDecl(Id(toAsciiCode), [VarDecl(Id(s), StringType, None, None)], Block([VarDecl(Id(ascii), ArrayType([96.0], StringType), None, ArrayLit(StringLit( ), StringLit(!), StringLit('"), StringLit(#), StringLit($), StringLit(%), StringLit(&), StringLit(\\'), StringLit((), StringLit()), StringLit(*), StringLit(+), StringLit(,), StringLit(-), StringLit(.), StringLit(/), StringLit(0), StringLit(1), StringLit(2), StringLit(3), StringLit(4), StringLit(5), StringLit(6), StringLit(7), StringLit(8), StringLit(9), StringLit(:), StringLit(;), StringLit(<), StringLit(=), StringLit(>), StringLit(?), StringLit(@), StringLit(A), StringLit(B), StringLit(C), StringLit(D), StringLit(E), StringLit(F), StringLit(G), StringLit(H), StringLit(I), StringLit(J), StringLit(K), StringLit(L), StringLit(M), StringLit(N), StringLit(O), StringLit(P), StringLit(Q), StringLit(R), StringLit(S), StringLit(T), StringLit(U), StringLit(V), StringLit(W), StringLit(X), StringLit(Y), StringLit(Z), StringLit([), StringLit(\\\\), StringLit(]), StringLit(^), StringLit(_), StringLit(`), StringLit(a), StringLit(b), StringLit(c), StringLit(d), StringLit(e), StringLit(f), StringLit(g), StringLit(h), StringLit(i), StringLit(j), StringLit(k), StringLit(l), StringLit(m), StringLit(n), StringLit(o), StringLit(p), StringLit(q), StringLit(r), StringLit(s), StringLit(t), StringLit(u), StringLit(v), StringLit(w), StringLit(x), StringLit(y), StringLit(z), StringLit({), StringLit(|), StringLit(}), StringLit(~), StringLit())), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(==, Id(s), ArrayCell(Id(ascii), [Id(i)])), NumLit(1.0), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))), Return(BinaryOp(+, Id(i), NumLit(32.0)))])), FuncDecl(Id(doNoThing), [VarDecl(Id(n), NumberType, None, None)], Return(Id(n))), FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, CallExpr(Id(toAsciiCode), [StringLit(a)]), NumLit(3.0)), NumLit(0.0)), If((BinaryOp(=, CallExpr(Id(toAssciiCode), [StringLit(b)]), BinaryOp(*, CallExpr(Id(doNoThing), [BinaryOp(/, CallExpr(Id(toAsciiCode), [StringLit(b)]), NumLit(3.0))]), NumLit(3.0))), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(3.0)])), NumLit(1.0), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, Id(LOOP_COUNT), UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0)))))))), [(BinaryOp(=, CallExpr(Id(toAsciiCode), [StringLit(c)]), Id(i)), If((BinaryOp(=, BinaryOp(%, BinaryOp(*, BinaryOp(*, Id(i), Id(i)), Id(i)), NumLit(128.0)), CallExpr(Id(toAsciiCode), [StringLit(H)])), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], AssignStmt(Id(i), BinaryOp(-, NumLit(1.0), UnaryOp(-, Id(i))))))))), [], None))], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input = """
number LOOP_COUNT <- 0
func toAsciiCode(string s)
begin 
string ascii[96] <- [" ","!","'"","#","$","%","&","\\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~",""]
number i<-0
for i until s == ascii[i] by 1
    i<-i+1
return i+32
end

func doNoThing(number n) return n
func main() begin
    number i<-0
    if (toAsciiCode("a") % 3 = 0)
        if (toAssciiCode("b") = doNoThing(toAsciiCode("b")/3)*3)
            for i until i<=doNoThing(3) by 1 LOOP_COUNT<- LOOP_COUNT ----1
        elif (toAsciiCode("c")=i) 
            if (i*i*i%128 = toAsciiCode("H"))
            for i until i<=doNoThing(100) by 1 
                if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                else for i until i<=doNoThing(100) by 1 
                    if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                    else i<-1--i 
            elif (false) i<-toAsciiCode("1")
            else i<-0
        elif (true) i<-1
end
"""
        expect = """Program([VarDecl(Id(LOOP_COUNT), NumberType, None, NumLit(0.0)), FuncDecl(Id(toAsciiCode), [VarDecl(Id(s), StringType, None, None)], Block([VarDecl(Id(ascii), ArrayType([96.0], StringType), None, ArrayLit(StringLit( ), StringLit(!), StringLit('"), StringLit(#), StringLit($), StringLit(%), StringLit(&), StringLit(\\'), StringLit((), StringLit()), StringLit(*), StringLit(+), StringLit(,), StringLit(-), StringLit(.), StringLit(/), StringLit(0), StringLit(1), StringLit(2), StringLit(3), StringLit(4), StringLit(5), StringLit(6), StringLit(7), StringLit(8), StringLit(9), StringLit(:), StringLit(;), StringLit(<), StringLit(=), StringLit(>), StringLit(?), StringLit(@), StringLit(A), StringLit(B), StringLit(C), StringLit(D), StringLit(E), StringLit(F), StringLit(G), StringLit(H), StringLit(I), StringLit(J), StringLit(K), StringLit(L), StringLit(M), StringLit(N), StringLit(O), StringLit(P), StringLit(Q), StringLit(R), StringLit(S), StringLit(T), StringLit(U), StringLit(V), StringLit(W), StringLit(X), StringLit(Y), StringLit(Z), StringLit([), StringLit(\\\\), StringLit(]), StringLit(^), StringLit(_), StringLit(`), StringLit(a), StringLit(b), StringLit(c), StringLit(d), StringLit(e), StringLit(f), StringLit(g), StringLit(h), StringLit(i), StringLit(j), StringLit(k), StringLit(l), StringLit(m), StringLit(n), StringLit(o), StringLit(p), StringLit(q), StringLit(r), StringLit(s), StringLit(t), StringLit(u), StringLit(v), StringLit(w), StringLit(x), StringLit(y), StringLit(z), StringLit({), StringLit(|), StringLit(}), StringLit(~), StringLit())), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(==, Id(s), ArrayCell(Id(ascii), [Id(i)])), NumLit(1.0), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))), Return(BinaryOp(+, Id(i), NumLit(32.0)))])), FuncDecl(Id(doNoThing), [VarDecl(Id(n), NumberType, None, None)], Return(Id(n))), FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, CallExpr(Id(toAsciiCode), [StringLit(a)]), NumLit(3.0)), NumLit(0.0)), If((BinaryOp(=, CallExpr(Id(toAssciiCode), [StringLit(b)]), BinaryOp(*, CallExpr(Id(doNoThing), [BinaryOp(/, CallExpr(Id(toAsciiCode), [StringLit(b)]), NumLit(3.0))]), NumLit(3.0))), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(3.0)])), NumLit(1.0), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, Id(LOOP_COUNT), UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0)))))))), [(BinaryOp(=, CallExpr(Id(toAsciiCode), [StringLit(c)]), Id(i)), If((BinaryOp(=, BinaryOp(%, BinaryOp(*, BinaryOp(*, Id(i), Id(i)), Id(i)), NumLit(128.0)), CallExpr(Id(toAsciiCode), [StringLit(H)])), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], AssignStmt(Id(i), BinaryOp(-, NumLit(1.0), UnaryOp(-, Id(i))))))))), [(BooleanLit(False), AssignStmt(Id(i), CallExpr(Id(toAsciiCode), [StringLit(1)])))], AssignStmt(Id(i), NumLit(0.0)))), (BooleanLit(True), AssignStmt(Id(i), NumLit(1.0)))], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = """
func main() begin 
var i<-0
for i until i=1 by 1
    if (i=0) break 
end 
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(1.0)), NumLit(1.0), If((BinaryOp(=, Id(i), NumLit(0.0)), Break), [], None))]))])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = """
func main() begin 
var i<-0
for i until i=10 by 1
    begin 
        var j<--0.87e-4
        i <- i*j
        continue
    end
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), Block([VarDecl(Id(j), None, var, UnaryOp(-, NumLit(8.7e-05))), AssignStmt(Id(i), BinaryOp(*, Id(i), Id(j))), Continue]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = """
func integral(number a, number b,number c) return c*b-c*a 
func sin(number x,bool degree, number exactrate) begin 
    var pi <- 3.141592653589793238462643383279502884197
    if (degree) x<- x*pi/180
    x<- x%(2*pi)
    number pow <- x 
    dynamic i<-1
    dynamic fact <- 1
    dynamic res <- 2*x
    for i until i=exactrate by 2
    begin
        res <- res - pow/fact 
        pow <- pow * x * X
        fact <- fact*i*(i-1)
    end
    return res
end
func main() begin 
    var n1 <- 1
    var n2 <- 2
    var n3 <- 3
    var n4 <- 4
    var b1 <- true 
    var b2 <- fasle 
    var b3 <- not true 
    var b4 <- true or false 
    dynamic res 
    res <- ( integral((n1*2 + 2*n1*n2 - n3*-n4)*n1%n2/n3+n4--n1*sin(3.14,false,701)) > sin(n1*n2-n3%n4,n1=n2*3-n4+sin(n1,n2>n3,701*n2%1),701) ) or (not b1 and b2 and not b3 or b4) and (b1 and not b4 or b3 and not b2)
end
"""
        expect = """Program([FuncDecl(Id(integral), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None), VarDecl(Id(c), NumberType, None, None)], Return(BinaryOp(-, BinaryOp(*, Id(c), Id(b)), BinaryOp(*, Id(c), Id(a))))), FuncDecl(Id(sin), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(degree), BoolType, None, None), VarDecl(Id(exactrate), NumberType, None, None)], Block([VarDecl(Id(pi), None, var, NumLit(3.141592653589793)), If((Id(degree), AssignStmt(Id(x), BinaryOp(/, BinaryOp(*, Id(x), Id(pi)), NumLit(180.0)))), [], None), AssignStmt(Id(x), BinaryOp(%, Id(x), BinaryOp(*, NumLit(2.0), Id(pi)))), VarDecl(Id(pow), NumberType, None, Id(x)), VarDecl(Id(i), None, dynamic, NumLit(1.0)), VarDecl(Id(fact), None, dynamic, NumLit(1.0)), VarDecl(Id(res), None, dynamic, BinaryOp(*, NumLit(2.0), Id(x))), For(Id(i), BinaryOp(=, Id(i), Id(exactrate)), NumLit(2.0), Block([AssignStmt(Id(res), BinaryOp(-, Id(res), BinaryOp(/, Id(pow), Id(fact)))), AssignStmt(Id(pow), BinaryOp(*, BinaryOp(*, Id(pow), Id(x)), Id(X))), AssignStmt(Id(fact), BinaryOp(*, BinaryOp(*, Id(fact), Id(i)), BinaryOp(-, Id(i), NumLit(1.0))))])), Return(Id(res))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n1), None, var, NumLit(1.0)), VarDecl(Id(n2), None, var, NumLit(2.0)), VarDecl(Id(n3), None, var, NumLit(3.0)), VarDecl(Id(n4), None, var, NumLit(4.0)), VarDecl(Id(b1), None, var, BooleanLit(True)), VarDecl(Id(b2), None, var, Id(fasle)), VarDecl(Id(b3), None, var, UnaryOp(not, BooleanLit(True))), VarDecl(Id(b4), None, var, BinaryOp(or, BooleanLit(True), BooleanLit(False))), VarDecl(Id(res), None, dynamic, None), AssignStmt(Id(res), BinaryOp(and, BinaryOp(or, BinaryOp(>, CallExpr(Id(integral), [BinaryOp(-, BinaryOp(+, BinaryOp(/, BinaryOp(%, BinaryOp(*, BinaryOp(-, BinaryOp(+, BinaryOp(*, Id(n1), NumLit(2.0)), BinaryOp(*, BinaryOp(*, NumLit(2.0), Id(n1)), Id(n2))), BinaryOp(*, Id(n3), UnaryOp(-, Id(n4)))), Id(n1)), Id(n2)), Id(n3)), Id(n4)), BinaryOp(*, UnaryOp(-, Id(n1)), CallExpr(Id(sin), [NumLit(3.14), BooleanLit(False), NumLit(701.0)])))]), CallExpr(Id(sin), [BinaryOp(-, BinaryOp(*, Id(n1), Id(n2)), BinaryOp(%, Id(n3), Id(n4))), BinaryOp(=, Id(n1), BinaryOp(+, BinaryOp(-, BinaryOp(*, Id(n2), NumLit(3.0)), Id(n4)), CallExpr(Id(sin), [Id(n1), BinaryOp(>, Id(n2), Id(n3)), BinaryOp(%, BinaryOp(*, NumLit(701.0), Id(n2)), NumLit(1.0))]))), NumLit(701.0)])), BinaryOp(or, BinaryOp(and, BinaryOp(and, UnaryOp(not, Id(b1)), Id(b2)), UnaryOp(not, Id(b3))), Id(b4))), BinaryOp(and, BinaryOp(or, BinaryOp(and, Id(b1), UnaryOp(not, Id(b4))), Id(b3)), UnaryOp(not, Id(b2)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = """
func test_looping(string a[1, 2], number __[0], bool cc_c)
begin
    if (a > b)
        for a until a + 1 by b + 1 if (a > b)
                if (a > b) number c
                elif (a > b) number c
                elif (a > b) number c
                else number c
            else
                break
    else
        for a until a > b by a * b / c
            for a until ssss[1, 2] by foo("hey", true, false, 1.e-3)
                if (a > b) number c
                else number c
end
"""
        expect = """Program([FuncDecl(Id(test_looping), [VarDecl(Id(a), ArrayType([1.0, 2.0], StringType), None, None), VarDecl(Id(__), ArrayType([0.0], NumberType), None, None), VarDecl(Id(cc_c), BoolType, None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), For(Id(a), BinaryOp(+, Id(a), NumLit(1.0)), BinaryOp(+, Id(b), NumLit(1.0)), If((BinaryOp(>, Id(a), Id(b)), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), (BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None))), [], Break))), [], For(Id(a), BinaryOp(>, Id(a), Id(b)), BinaryOp(/, BinaryOp(*, Id(a), Id(b)), Id(c)), For(Id(a), ArrayCell(Id(ssss), [NumLit(1.0), NumLit(2.0)]), CallExpr(Id(foo), [StringLit(hey), BooleanLit(True), BooleanLit(False), NumLit(0.001)]), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input = """
func foo(number a)
begin
    if ((a=1) or (a=0)) return 1
    return a*foo(a)
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(foo(3))]]

func main()
begin
    number a<- arr[foo(1),foo(3)%3]
    return
end
"""
        expect = """Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(=, Id(a), NumLit(1.0)), BinaryOp(=, Id(a), NumLit(0.0))), Return(NumLit(1.0))), [], None), Return(BinaryOp(*, Id(a), CallExpr(Id(foo), [Id(a)])))])), VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(*, NumLit(5.0), NumLit(6.0)), BinaryOp(%, NumLit(7.0), NumLit(2.0)), BinaryOp(*, UnaryOp(-, NumLit(3.13e-06)), CallExpr(Id(foo), [CallExpr(Id(foo), [NumLit(3.0)])]))))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(arr), [CallExpr(Id(foo), [NumLit(1.0)]), BinaryOp(%, CallExpr(Id(foo), [NumLit(3.0)]), NumLit(3.0))])), Return()]))])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input = """
func main()
begin
    number _ <- readNumber()
    number __<- readNumber()
    for _ until _*_ = _+_*_-2*_ by _+_
        if (_) 
            for _ until _/(_*_)%_ < _/(_*_+_) by _/_
                if (_*_<_+_) begin
                end
                elif (__<_) if ((__+_/__ = _%__) and (__*_< -1)) 
                    for _ until _/(_*_)%_ < _/(_*_+_) by _/_ 
                        if (true) break 
                        else continue
                else break
        elif (true) continue
        else break
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(_), NumberType, None, CallExpr(Id(readNumber), [])), VarDecl(Id(__), NumberType, None, CallExpr(Id(readNumber), [])), For(Id(_), BinaryOp(=, BinaryOp(*, Id(_), Id(_)), BinaryOp(-, BinaryOp(+, Id(_), BinaryOp(*, Id(_), Id(_))), BinaryOp(*, NumLit(2.0), Id(_)))), BinaryOp(+, Id(_), Id(_)), If((Id(_), For(Id(_), BinaryOp(<, BinaryOp(%, BinaryOp(/, Id(_), BinaryOp(*, Id(_), Id(_))), Id(_)), BinaryOp(/, Id(_), BinaryOp(+, BinaryOp(*, Id(_), Id(_)), Id(_)))), BinaryOp(/, Id(_), Id(_)), If((BinaryOp(<, BinaryOp(*, Id(_), Id(_)), BinaryOp(+, Id(_), Id(_))), Block([])), [(BinaryOp(<, Id(__), Id(_)), If((BinaryOp(and, BinaryOp(=, BinaryOp(+, Id(__), BinaryOp(/, Id(_), Id(__))), BinaryOp(%, Id(_), Id(__))), BinaryOp(<, BinaryOp(*, Id(__), Id(_)), UnaryOp(-, NumLit(1.0)))), For(Id(_), BinaryOp(<, BinaryOp(%, BinaryOp(/, Id(_), BinaryOp(*, Id(_), Id(_))), Id(_)), BinaryOp(/, Id(_), BinaryOp(+, BinaryOp(*, Id(_), Id(_)), Id(_)))), BinaryOp(/, Id(_), Id(_)), If((BooleanLit(True), Break), [], Continue))), [], Break)), (BooleanLit(True), Continue)], Break))), [], None))]))])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input = """
func main() 
begin
    dynamic a
    a <- ((A or B and C + 3*2%4/3)<=(not(-1+foo(x+y*(z-1)))))...(x!=y)
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, dynamic, None), AssignStmt(Id(a), BinaryOp(..., BinaryOp(<=, BinaryOp(and, BinaryOp(or, Id(A), Id(B)), BinaryOp(+, Id(C), BinaryOp(/, BinaryOp(%, BinaryOp(*, NumLit(3.0), NumLit(2.0)), NumLit(4.0)), NumLit(3.0)))), UnaryOp(not, BinaryOp(+, UnaryOp(-, NumLit(1.0)), CallExpr(Id(foo), [BinaryOp(+, Id(x), BinaryOp(*, Id(y), BinaryOp(-, Id(z), NumLit(1.0))))])))), BinaryOp(!=, Id(x), Id(y))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
        input = """
func main() begin 
number a<- readNumber()
if (a<0) 
    if (-a%2 = 0) 
        begin
        end
    else if (a<50) return
        elif (a<100) return
        else return 
elif (a>10) 
    begin 
    end 
else return
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, CallExpr(Id(readNumber), [])), If((BinaryOp(<, Id(a), NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, UnaryOp(-, Id(a)), NumLit(2.0)), NumLit(0.0)), Block([])), [], If((BinaryOp(<, Id(a), NumLit(50.0)), Return()), [(BinaryOp(<, Id(a), NumLit(100.0)), Return())], Return()))), [(BinaryOp(>, Id(a), NumLit(10.0)), Block([]))], Return())]))])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = """
func inc(number x) return x+1
number a <-  inc(inc(inc(inc(3))))
"""
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(x), NumberType, None, None)], Return(BinaryOp(+, Id(x), NumLit(1.0)))), VarDecl(Id(a), NumberType, None, CallExpr(Id(inc), [CallExpr(Id(inc), [CallExpr(Id(inc), [CallExpr(Id(inc), [NumLit(3.0)])])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = """
func xor(bool a, bool b) return (a and not b) or (not a and b)
bool a<- xor(true,false) or xor(false,true) or not (xor(true,true))
"""
        expect = """Program([FuncDecl(Id(xor), [VarDecl(Id(a), BoolType, None, None), VarDecl(Id(b), BoolType, None, None)], Return(BinaryOp(or, BinaryOp(and, Id(a), UnaryOp(not, Id(b))), BinaryOp(and, UnaryOp(not, Id(a)), Id(b))))), VarDecl(Id(a), BoolType, None, BinaryOp(or, BinaryOp(or, CallExpr(Id(xor), [BooleanLit(True), BooleanLit(False)]), CallExpr(Id(xor), [BooleanLit(False), BooleanLit(True)])), UnaryOp(not, CallExpr(Id(xor), [BooleanLit(True), BooleanLit(True)]))))])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = """
func printSolution(number board[100, 100], number n)
begin
    var i <- 0
    var j <- 0
	for i until i >= n by 1 begin
		for j until j >= n by 1
            if (board[i, j]) writeString("Q ")
		    else writeString(". ")
		printf("\\n")
	end
end

func isSafe(number board[100, 100], number n, number row, number col) begin
	var i <- 0
    var j <- 0
	for i until i >= col by 1
		if (board[row, i])
			return false
    
    i <- row
    j <- col
	for i until ((i < 0) or (j < 0)) by -1 begin
		if (board[i, j])
			return false
        j <- j - 1
    end
    
    i <- row
    j <- col
	for i until ((i >= n) or (j < 0)) by 1 begin
		if (board[i, j])
			return false
        j <- j - 1
    end
	
    return true
end

func solverec(number board[100, 100], number col, number n) begin
    if (col >= n) return true
    
    var i <- 0
    for i until i >= n by 1 begin
		if (isSafe(board, n, i, col)) begin
			board[i, col] <- 1
			if (solverec(board, col + 1, n)) return true
			board[i, col] <- 0
		end
	end
	
    return false
end

func solve(number n)
begin
    number board[100, 100]
    var i <- 0
    var j <- 0
    for i until i >= n by 1
        for j until j >= n by 1
            board[i, j] <- 0
    
    if (not solverec(board, 0, n)) writeString("No solution")
    else printSolution(board, n)
end
"""
        expect = """Program([FuncDecl(Id(printSolution), [VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), Block([For(Id(j), BinaryOp(>=, Id(j), Id(n)), NumLit(1.0), If((ArrayCell(Id(board), [Id(i), Id(j)]), CallStmt(Id(writeString), [StringLit(Q )])), [], CallStmt(Id(writeString), [StringLit(. )]))), CallStmt(Id(printf), [StringLit(\\n)])]))])), FuncDecl(Id(isSafe), [VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(row), NumberType, None, None), VarDecl(Id(col), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(col)), NumLit(1.0), If((ArrayCell(Id(board), [Id(row), Id(i)]), Return(BooleanLit(False))), [], None)), AssignStmt(Id(i), Id(row)), AssignStmt(Id(j), Id(col)), For(Id(i), BinaryOp(or, BinaryOp(<, Id(i), NumLit(0.0)), BinaryOp(<, Id(j), NumLit(0.0))), UnaryOp(-, NumLit(1.0)), Block([If((ArrayCell(Id(board), [Id(i), Id(j)]), Return(BooleanLit(False))), [], None), AssignStmt(Id(j), BinaryOp(-, Id(j), NumLit(1.0)))])), AssignStmt(Id(i), Id(row)), AssignStmt(Id(j), Id(col)), For(Id(i), BinaryOp(or, BinaryOp(>=, Id(i), Id(n)), BinaryOp(<, Id(j), NumLit(0.0))), NumLit(1.0), Block([If((ArrayCell(Id(board), [Id(i), Id(j)]), Return(BooleanLit(False))), [], None), AssignStmt(Id(j), BinaryOp(-, Id(j), NumLit(1.0)))])), Return(BooleanLit(True))])), FuncDecl(Id(solverec), [VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(col), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(>=, Id(col), Id(n)), Return(BooleanLit(True))), [], None), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), Block([If((CallExpr(Id(isSafe), [Id(board), Id(n), Id(i), Id(col)]), Block([AssignStmt(ArrayCell(Id(board), [Id(i), Id(col)]), NumLit(1.0)), If((CallExpr(Id(solverec), [Id(board), BinaryOp(+, Id(col), NumLit(1.0)), Id(n)]), Return(BooleanLit(True))), [], None), AssignStmt(ArrayCell(Id(board), [Id(i), Id(col)]), NumLit(0.0))])), [], None)])), Return(BooleanLit(False))])), FuncDecl(Id(solve), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), For(Id(j), BinaryOp(>=, Id(j), Id(n)), NumLit(1.0), AssignStmt(ArrayCell(Id(board), [Id(i), Id(j)]), NumLit(0.0)))), If((UnaryOp(not, CallExpr(Id(solverec), [Id(board), NumLit(0.0), Id(n)])), CallStmt(Id(writeString), [StringLit(No solution)])), [], CallStmt(Id(printSolution), [Id(board), Id(n)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """
func main() 
begin 
    number a[4,6,7,8]
    a[3,2,1,ahahaha(4)] <- 1
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), NumLit(2.0), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = """
func main()
begin
    number b<-1
    var a<- --------[1,2]*----------------b
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(a), None, var, BinaryOp(*, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, ArrayLit(NumLit(1.0), NumLit(2.0)))))))))), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(b)))))))))))))))))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = """
func main()
begin
    number b<-1
    var a<- --------1*----------------b
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(a), None, var, BinaryOp(*, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0))))))))), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(b)))))))))))))))))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = """
func main() 
begin 
    bool a<-true 
    bool b<-false 
    if (not a) 
        if (b) writeString("b is correct")
        else writeString("b is not correct")
    else writeString("a is correct")
    return
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, BooleanLit(True)), VarDecl(Id(b), BoolType, None, BooleanLit(False)), If((UnaryOp(not, Id(a)), If((Id(b), CallStmt(Id(writeString), [StringLit(b is correct)])), [], CallStmt(Id(writeString), [StringLit(b is not correct)]))), [], CallStmt(Id(writeString), [StringLit(a is correct)])), Return()]))])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = """
func main()
begin 
if(1) return 
elif (2) 
    if (3) return 
    elif (4) return 
    elif (5) return 
    else return
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), Return()), [(NumLit(2.0), If((NumLit(3.0), Return()), [(NumLit(4.0), Return()), (NumLit(5.0), Return())], Return()))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = """
func main() 
begin 
    if (1) number a[3,2] <- [[1,2],[3,4],[5,6]]
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(a), ArrayType([3.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(5.0), NumLit(6.0))))), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = """
func main() 
begin 
    for i until i!=0 by 1 dynamic i
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(!=, Id(i), NumLit(0.0)), NumLit(1.0), VarDecl(Id(i), None, dynamic, None))]))])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input = """
func main() 
begin 
    if (1) string a[3,2] <- [[1,2],[3,4],[5,6]]
    else number b[4,4,4]
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(a), ArrayType([3.0, 2.0], StringType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(5.0), NumLit(6.0))))), [], VarDecl(Id(b), ArrayType([4.0, 4.0, 4.0], NumberType), None, None))]))])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_3999(self):
        input = """func main ()
        begin
            writeNumber(1 + 2 + 3)
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [],
                                       Block([If(BooleanLiteral(True),
                                                 Continue(),
                                                 [(BooleanLiteral(False),
                                                   If(BooleanLiteral(True), Break(), [(BooleanLiteral(True), Break()),
                                                                                      (BooleanLiteral(True), Break())],
                                                      None))], None)])
                                       )
                              ]
                             )
                     )
        print(expect)
        self.assertTrue(TestAST.test(input, expect, 3999))
