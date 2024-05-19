import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_500(self):
    #     input = """func main ()
    #     begin
    #         writeNumber(1)
    #     end
    #     """
    #     expect = "1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 500))

    # def test_501(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeNumber(1)
    #         writeBool(true)
    #         writeString("minhat")
    #     end
    #     """
    #     expect = "1.0trueminhat"
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))

    # def test_502(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeNumber(1.0)
    #         writeBool(false)
    #         writeString("")
    #     end
    #     """
    #     expect = "1.0false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))

    # def test_503(self):
    #     input = """
    #     number a <- 1
    #     func main ()
    #     begin
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))

    # def test_504(self):
    #     input = """
    #     number a <- 1
    #     func main ()
    #     begin
    #         number a <- 2
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))

    # def test_505(self):
    #     input = """
    #     number a <- 1
    #     func main ()
    #     begin
    #         begin
    #             number a <- 2
    #         end
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))

    # def test_506(self):
    #     input = """
    #     number a <- 1
    #     func main ()
    #     begin
    #         begin
    #             number a <- 2
    #             writeNumber(a)
    #         end
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "2.01.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))

    # def test_507(self):
    #     input = """
    #     bool a
    #     func main ()
    #     begin
    #         bool b <- true
    #         begin
    #             a <- b
    #         end
    #         writeBool(a)
    #     end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))

    # def test_508(self):
    #     input = """
    #     string a
    #     func main ()
    #     begin
    #         string b <- "minhat"
    #         begin
    #             a <- b
    #         end
    #         writeString(a)
    #     end
    #     """
    #     expect = "minhat"
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))

    # def test_509(self):
    #     input = """
    #     number a <- 1
    #     func foo(number a)
    #     begin
    #         writeNumber(a)
    #     end
    #     func main ()
    #     begin
    #         foo(2)
    #     end
    #     """
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))

    # def test_510(self):
    #     input = """
    #     number a <-1
    #     func foo(number a)
    #     begin
    #         number a <- 3
    #         writeNumber(a)
    #     end
    #     func main ()
    #     begin
    #         foo(2)
    #     end
    #     """
    #     expect = "3.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))

    # def test_511(self):
    #     input = """
    #     number a <-1
    #     func foo(number a)
    #     begin
    #         writeNumber(a)
    #         number a <- 3
    #         writeNumber(a)
    #     end
    #     func main ()
    #     begin
    #         foo(2)
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "2.03.01.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))

    # def test_512(self):
    #     input = """
    #     number a <-1
    #     func foo()
    #     begin
    #         a <- 3
    #     end
    #     func main ()
    #     begin
    #         foo()
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "3.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))

    # def test_513(self):
    #     input = """
    #     number a <- 1
    #     func foo()
    #     begin
    #         begin
    #             number a <- 2
    #         end
    #         writeNumber(a)
    #         a <- 3
    #     end
    #     func main ()
    #     begin
    #         foo()
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "1.03.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))

    # def test_514(self):
    #     input = """
    #     number a <- 1
    #     func foo()
    #     begin
    #         a <- 3
    #         writeNumber(a)
    #     end
    #     func main ()
    #     begin
    #         number a <- 2
    #         foo()
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "3.02.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))

    # def test_515(self):
    #     input = """
    #     number a
    #     func foo()
    #     func main ()
    #     begin
    #         foo()
    #         writeNumber(a)
    #     end
    #     func foo()
    #     begin
    #         a <- 3
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "3.03.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))

    # def test_516(self):
    #     input = """
    #     func foo(number a)
    #     begin
    #         return a
    #     end
    #     func main ()
    #     begin
    #         writeNumber(foo(2))
    #     end
    #     """
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))

    # def test_517(self):
    #     input = """
    #     func foo(number a)
    #     begin
    #         return true
    #     end
    #     func main ()
    #     begin
    #         writeBool(foo(2))
    #     end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))

    # def test_518(self):
    #     input = """
    #     func foo(string a)
    #     begin
    #         return a
    #     end
    #     func main ()
    #     begin
    #         writeString(foo("nhat"))
    #     end
    #     """
    #     expect = "nhat"
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))

    # def test_519(self):
    #     input = """
    #     func main ()
    #     begin
    #         string a <- readString()
    #         writeString(a)
    #     end
    #     """
    #     expect = "Dang Duong Minh Nhat"
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))

    # def test_520(self):
    #     input = """
    #     func main ()
    #     begin
    #         number a <- readNumber()
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "-1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))

    # def test_521(self):
    #     input = """
    #     func main ()
    #     begin
    #         bool a <- readBool()
    #         writeBool(a)
    #     end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))

    # def test_522(self):
    #     input = """
    #     func foo()
    #         return true
    #     func main ()
    #     begin
    #         bool a <- foo()
    #         writeBool(a)
    #     end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))

    # def test_523(self):
    #     input = """
    #     func foo()
    #         return "minhat"
    #     func main ()
    #     begin
    #         string a <- foo()
    #         writeString(a)
    #     end
    #     """
    #     expect = "minhat"
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))

    # def test_524(self):
    #     input = """
    #     func foo(number a, number c)
    #         return a
    #     func main ()
    #     begin
    #         number a <- foo(1, 2)
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))

    # def test_525(self):
    #     input = """
    #     number c <- 5
    #     func foo(number a, number c)
    #     begin
    #         return c
    #     end
    #     func main ()
    #     begin
    #         number a <- foo(1, 2)
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))

    # def test_526(self):
    #     input = """
    #     number c <- 5
    #     func foo(number a)
    #     begin
    #         return c
    #     end
    #     func main ()
    #     begin
    #         number a <- foo(1)
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "5.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))

    # def test_527(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeNumber(1 + 1)
    #         writeNumber(1 - 1)
    #         writeNumber(1 * 2)
    #         writeNumber(1 / 2)
    #         writeNumber(7.5%3.5)
    #         writeNumber(7.8%3.38)
    #     end
    #     """
    #     expect = "2.00.02.00.50.51.04"
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))

    # def test_528(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeNumber(1 + 1 + 1)
    #         writeNumber(1 + 1 * 3 - 1 * 2 / 2)
    #         writeNumber(2 * 3 % 2)
    #     end
    #     """
    #     expect = "3.03.00.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))

    # def test_529(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeBool(1 > 2)
    #         writeBool(2 > 1)
    #         writeBool(1 > 1)
    #     end
    #     """
    #     expect = "falsetruefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))

    # def test_530(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeBool(1 >= 2)
    #         writeBool(2 >= 1)
    #         writeBool(1 >= 1)
    #     end
    #     """
    #     expect = "falsetruetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))

    # def test_531(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeBool(1 < 2)
    #         writeBool(2 < 1)
    #         writeBool(1 < 1)
    #     end
    #     """
    #     expect = "truefalsefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))

    # def test_532(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeBool(1 <= 2)
    #         writeBool(2 <= 1)
    #         writeBool(1 <= 1)
    #     end
    #     """
    #     expect = "truefalsetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))

    # def test_533(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeBool(1 != 2)
    #         writeBool(2 != 1)
    #         writeBool(1 != 1)
    #     end
    #     """
    #     expect = "truetruefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_534(self):
        input = """
        func main ()
        begin
            writeBool(1 = 2) 
            writeBool(2 = 1) 
            writeBool(1 = 1) 
        end
        """
        expect = "falsefalsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    # def test_535(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeBool(true and true)
    #         writeBool(true and false)
    #         writeBool(false and true)
    #         writeBool(false and false)
    #     end
    #     """
    #     expect = "truefalsefalsefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))

    # def test_536(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeBool(true or true)
    #         writeBool(true or false)
    #         writeBool(false or true)
    #         writeBool(false or false)
    #     end
    #     """
    #     expect = "truetruetruefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 536))

    # def test_537(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeBool(true or true and false or true)
    #     end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 537))

    # def test_538(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeString("Minh" ... "Nhat")
    #     end
    #     """
    #     expect = "MinhNhat"
    #     self.assertTrue(TestCodeGen.test(input, expect, 538))

    # def test_539(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeBool("minh" == "nhat")
    #         writeBool("nhat" == "nhat")
    #     end
    #     """
    #     expect = "falsetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 539))

    # def test_540(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeBool(not not true)
    #         writeBool(not true)
    #         writeBool(not false)
    #     end
    #     """
    #     expect = "truefalsetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 540))

    # def test_541(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeNumber(--1)
    #         writeNumber(-1)
    #     end
    #     """
    #     expect = "1.0-1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 541))
