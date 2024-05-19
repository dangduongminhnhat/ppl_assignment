import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_100(self):
        input = """func main()
begin
## This is comment.
a <- 5
end
"""
        expect = """func,main,(,),
,begin,
,
,a,<-,5,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 100))

    def test_101(self):
        input = """func main()
begin
a <- "This is a string containing tab \\t"
b <- "He asked me: '"Where is John?'""
end
"""
        expect = """func,main,(,),
,begin,
,a,<-,This is a string containing tab \\t,
,b,<-,He asked me: '"Where is John?'",
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 101))

    def test_102(self):
        input = """func main()
begin
number a[5] <- [1, 2, 3, 4, 5]
number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
end
"""
        expect = """func,main,(,),
,begin,
,number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],
,number,b,[,2,,,3,],<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],],
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test_103(self):
        input = """func main()
begin
a[3 + foo(2)] <- a[b[2, 3]] + 4
end
"""
        expect = """func,main,(,),
,begin,
,a,[,3,+,foo,(,2,),],<-,a,[,b,[,2,,,3,],],+,4,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test_104(self):
        input = """func foo(number a[5], string b)
begin
var i <- 0
for i until i >= 5 by 1
begin
a[i] <- i * i + 5
end
return -1
end
"""
        expect = """func,foo,(,number,a,[,5,],,,string,b,),
,begin,
,var,i,<-,0,
,for,i,until,i,>=,5,by,1,
,begin,
,a,[,i,],<-,i,*,i,+,5,
,end,
,return,-,1,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 104))

    def test_105(self):
        input = """func foo(number a[5], string b)
begin
aPI <- 3.14
l[3] <- value * aPi
end
"""
        expect = """func,foo,(,number,a,[,5,],,,string,b,),
,begin,
,aPI,<-,3.14,
,l,[,3,],<-,value,*,aPi,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test_106(self):
        input = """func foo(number a[5], string b)
begin
var i <- 0
for i until i >= 10 by 1
writeNumbe(i)
end
"""
        expect = """func,foo,(,number,a,[,5,],,,string,b,),
,begin,
,var,i,<-,0,
,for,i,until,i,>=,10,by,1,
,writeNumbe,(,i,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 106))

    def test_107(self):
        input = """func foo(number a[5], string b)
begin
number r
number s
r <- 2.0
number a[5]
number b[5]
s <- r * r * 3.14
a[0] <- s
end
"""
        expect = """func,foo,(,number,a,[,5,],,,string,b,),
,begin,
,number,r,
,number,s,
,r,<-,2.0,
,number,a,[,5,],
,number,b,[,5,],
,s,<-,r,*,r,*,3.14,
,a,[,0,],<-,s,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 107))

    def test_108(self):
        input = """func areDivisors(number num1, number num2)
return ((num1 % num2 = 0) or (num2 % num1 = 0))
func main()
begin
var num1 <- readNumber()
var num2 <- readNumber()
if (areDivisors(num1, num2)) writeString("Yes")
else writeString("No")
end
"""
        expect = """func,areDivisors,(,number,num1,,,number,num2,),
,return,(,(,num1,%,num2,=,0,),or,(,num2,%,num1,=,0,),),
,func,main,(,),
,begin,
,var,num1,<-,readNumber,(,),
,var,num2,<-,readNumber,(,),
,if,(,areDivisors,(,num1,,,num2,),),writeString,(,Yes,),
,else,writeString,(,No,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 108))

    def test_109(self):
        input = """func isPrime(number x)
func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("Yes")
else writeString("No")
end
"""
        expect = """func,isPrime,(,number,x,),
,func,main,(,),
,begin,
,number,x,<-,readNumber,(,),
,if,(,isPrime,(,x,),),writeString,(,Yes,),
,else,writeString,(,No,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 109))

    def test_110(self):
        input = """func isPrime(number x)
begin
if (x <= 1) return false
var i <- 2
for i until i > x / 2 by 1
begin
if (x % i = 0) return false
end
return true
end
"""
        expect = """func,isPrime,(,number,x,),
,begin,
,if,(,x,<=,1,),return,false,
,var,i,<-,2,
,for,i,until,i,>,x,/,2,by,1,
,begin,
,if,(,x,%,i,=,0,),return,false,
,end,
,return,true,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 110))

    def test_111(self):
        input = """## this program has only two lines: this comment and the following function declaration.

func main() 
begin
writeString("Hello world")
end
"""
        expect = """
,
,func,main,(,),
,begin,
,writeString,(,Hello world,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 111))

    def test_112(self):
        input = """a\n\n\n#"""
        expect = """a,
,
,
,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 112))

    def test_113(self):
        input = """\"Day la \'Hoa\' \""""
        expect = """Day la \'Hoa\' ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 113))

    def test_114(self):
        input = """\"Day la \\\'Hoa\\\'\""""
        expect = """Day la \\\'Hoa\\\',<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 114))

    def test_115(self):
        input = """\"He asked me: \'\""""
        expect = """Unclosed String: He asked me: \'\""""
        self.assertTrue(TestLexer.test(input, expect, 115))

    def test_116(self):
        input = """\"Hello \\\\ \\\""""
        expect = """Illegal Escape In String: Hello \\\\ \\\""""
        self.assertTrue(TestLexer.test(input, expect, 116))

    def test_117(self):
        input = """\"abc'de\""""
        expect = """abc\'de,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 117))

    def test_118(self):
        input = """func main()
        begin
        string c <- "\mmmp"
        end
        """
        expect = """func,main,(,),
,begin,
,string,c,<-,Illegal Escape In String: \\m"""
        self.assertTrue(TestLexer.test(input, expect, 118))

    def test_119(self):
        input = """func foo(number a[1,2,3])
        """
        expect = """func,foo,(,number,a,[,1,,,2,,,3,],),
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 119))

    def test_120(self):
        input = """\"\'\""""
        expect = """Unclosed String: \'\""""
        self.assertTrue(TestLexer.test(input, expect, 120))

    def test_121(self):
        input = """func main()
begin
number arr["string",abc()] <- [[1,2],[2,3]]
end
        """
        expect = """func,main,(,),
,begin,
,number,arr,[,string,,,abc,(,),],<-,[,[,1,,,2,],,,[,2,,,3,],],
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 121))

    def test_122(self):
        input = """func main()
begin
number a[1,"abc",true] <- 1
end
        """
        expect = """func,main,(,),
,begin,
,number,a,[,1,,,abc,,,true,],<-,1,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 122))

    def test_123(self):
        input = """bool a\n\n\n"""
        expect = """bool,a,
,
,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 123))

    def test_124(self):
        input = """func main() return
        """
        expect = """func,main,(,),return,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 124))

    def test_125(self):
        input = """ "This is Test \\t" """
        expect = """This is Test \\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 125))

    def test_126(self):
        input = """func main()
begin
number x <- [1, 2, 3]
var x <- [1, 2, 3]
dynamic x <- [1, 2, 3]
number x
x <- [1, 2, 3]
number x[3]
x <- [1, 2, 3]
end
"""
        expect = """func,main,(,),
,begin,
,number,x,<-,[,1,,,2,,,3,],
,var,x,<-,[,1,,,2,,,3,],
,dynamic,x,<-,[,1,,,2,,,3,],
,number,x,
,x,<-,[,1,,,2,,,3,],
,number,x,[,3,],
,x,<-,[,1,,,2,,,3,],
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 126))

    def test_127(self):
        input = """func main()
begin
arr["BTL"] <- true

arr[0] <- b["PPL",2]

x <- "qua" + 3 

end
"""
        expect = """func,main,(,),
,begin,
,arr,[,BTL,],<-,true,
,
,arr,[,0,],<-,b,[,PPL,,,2,],
,
,x,<-,qua,+,3,
,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 127))

    def test_128(self):
        input = "true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"
        expect = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 128))

    def test_129(self):
        input = "+-*/%= <- != < <= > >= ... =="
        expect = "+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 129))

    def test_130(self):
        self.assertTrue(TestLexer.test(
            "A _ a az AZ aZ _a a_ a1 _1 A1", "A,_,a,az,AZ,aZ,_a,a_,a1,_1,A1,<EOF>", 130))

    def test_131(self):
        self.assertTrue(TestLexer.test("19Nhat", "19,Nhat,<EOF>", 131))

    def test_132(self):
        self.assertTrue(TestLexer.test("01Nhat", "01,Nhat,<EOF>", 132))

    def test_133(self):
        input = "0 -0 199 001 012. 12. 0. 12.3 12.3e3 12.3e-30 2.e3 0.e-30 31e+3 31e-3 0e+3 0e-3"
        expect = "0,-,0,199,001,012.,12.,0.,12.3,12.3e3,12.3e-30,2.e3,0.e-30,31e+3,31e-3,0e+3,0e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 133))

    def test_134(self):
        self.assertTrue(TestLexer.test(".12e-3", "Error Token .", 134))

    def test_135(self):
        self.assertTrue(TestLexer.test("12.2h-3", "12.2,h,-,3,<EOF>", 135))

    def test_136(self):
        input = """ "Minh Nhat" """
        expect = "Minh Nhat,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))

    def test_137(self):
        self.assertTrue(TestLexer.test(""" "" """, ",<EOF>", 137))

    def test_138(self):
        input = """ "' \\b \\f \\r \\n \\t \\\\ Dang \\b \\f \\r \\n \\t \\\\  Nhat \\b \\f \\r \\n \\t \\\\" """
        expect = "' \\b \\f \\r \\n \\t \\\\ Dang \\b \\f \\r \\n \\t \\\\  Nhat \\b \\f \\r \\n \\t \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))

    def test_139(self):
        self.assertTrue(TestLexer.test(
            """ "'"Dang '" Nhat '' '"" """, "'\"Dang '\" Nhat '' '\",<EOF>", 139))

    def test_140(self):
        self.assertTrue(TestLexer.test(""" "Dang \n" """,
                        "Unclosed String: Dang ", 140))

    def test_141(self):
        self.assertTrue(TestLexer.test(
            """ "Dang \n Nhat" """, "Unclosed String: Dang ", 141))

    def test_142(self):
        self.assertTrue(TestLexer.test(
            """ "Dang  """, "Unclosed String: Dang  ", 142))

    def test_143(self):
        self.assertTrue(TestLexer.test(""" "Dang \\n \n """,
                        "Unclosed String: Dang \\n ", 143))

    def test_144(self):
        self.assertTrue(TestLexer.test(""" "Dang ' \\n \\b """,
                        "Unclosed String: Dang ' \\n \\b ", 144))

    def test_145(self):
        self.assertTrue(TestLexer.test(""" "Nhat ' \\1  """,
                        "Illegal Escape In String: Nhat ' \\1", 145))

    def test_146(self):
        self.assertTrue(TestLexer.test(""" "Nhat \\2 \\n \n """,
                        "Illegal Escape In String: Nhat \\2", 146))

    def test_147(self):
        self.assertTrue(TestLexer.test(""" "Nhat \\e \\n \\r """,
                        "Illegal Escape In String: Nhat \\e", 147))

    def test_148(self):
        self.assertTrue(TestLexer.test("## Dang Nhat", "<EOF>", 148))

    def test_149(self):
        self.assertTrue(TestLexer.test("###", "<EOF>", 149))

    def test_150(self):
        self.assertTrue(TestLexer.test("a##1", "a,<EOF>", 150))

    def test_151(self):
        self.assertTrue(TestLexer.test("a#", "a,Error Token #", 151))

    def test_152(self):
        self.assertTrue(TestLexer.test("a\n##1\nb", "a,\n,\n,b,<EOF>", 152))

    def test_153(self):
        self.assertTrue(TestLexer.test(
            "a\n\n\n#", "a,\n,\n,\n,Error Token #", 153))

    def test_154(self):
        input = """a
                    ## comment
                """
        expect = """a,
,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_155(self):
        input = "."
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 155))

    def test_156(self):
        input = ";"
        expect = "Error Token ;"
        self.assertTrue(TestLexer.test(input, expect, 156))

    def test_157(self):
        input = "{"
        expect = "Error Token {"
        self.assertTrue(TestLexer.test(input, expect, 157))

    def test_158(self):
        self.assertTrue(TestLexer.test("+1-2", "+,1,-,2,<EOF>", 158))

    def test_159(self):
        self.assertTrue(TestLexer.test(""" "Nhat \t \n" """,
                        "Unclosed String: Nhat 	 ", 159))

    def test_160(self):
        self.assertTrue(TestLexer.test(""" "Nhat \\" """,
                        "Illegal Escape In String: Nhat \\\"", 160))

    def test_161(self):
        self.assertTrue(TestLexer.test(""" "Nhat \\\n """,
                        "Illegal Escape In String: Nhat \\\n", 161))

    def test_162(self):
        self.assertTrue(TestLexer.test(""" "Nhat '\\ """,
                        "Illegal Escape In String: Nhat '\\ ", 162))

    def test_163(self):
        self.assertTrue(TestLexer.test(
            """ "Nhat \'" " """, "Nhat '\" ,<EOF>", 163))

    def test_164(self):
        self.assertTrue(TestLexer.test(""" "Nhat \\\'" " """,
                        "Nhat \\',Unclosed String:  ", 164))

    def test_165(self):
        self.assertTrue(TestLexer.test(""" "Nhat 
                                       " """, "Unclosed String: Nhat ", 165))

    def test_166(self):
        input = ""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 166))

    def test_167(self):
        input = "\"\'\"\\n\\t\\f\\b\\r\""
        expect = "\'\"\\n\\t\\f\\b\\r,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 167))

    def test_168(self):
        input = "####"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 168))

    def test_169(self):
        input = "12.13"
        expect = "12.13,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))

    def test_170(self):
        input = "func main() return 1"
        expect = "func,main,(,),return,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))

    def test_171(self):
        input = "a <- -b + 12.03e-12"
        expect = "a,<-,-,b,+,12.03e-12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))

    def test_172(self):
        input = """
0
0.0
199
12.
12.e-30
12.E+12
12.3
12.3e3
12.3e-30
012
"""
        expect = """
,0,
,0.0,
,199,
,12.,
,12.e-30,
,12.E+12,
,12.3,
,12.3e3,
,12.3e-30,
,012,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 172))

    def test_173(self):
        input = "true false true true false"
        expect = "true,false,true,true,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))

    def test_174(self):
        input = """\"This is a string containing tab \\t\""""
        expect = "This is a string containing tab \\t,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))

    def test_175(self):
        input = "\"He asked me: '\"Where is John?'\"\""
        expect = "He asked me: '\"Where is John?'\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))

    def test_176(self):
        input = """## This is a single comment.
a + b = 5"""
        expect = "\n,a,+,b,=,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))

    def test_177(self):
        input = "\"He asked me: '\"Where is John?'\"\""
        expect = "He asked me: '\"Where is John?'\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 177))

    def test_178(self):
        input = """s = "He said: \\x OK\""""
        expect = "s,=,Illegal Escape In String: He said: \\x"
        self.assertTrue(TestLexer.test(input, expect, 178))

    def test_179(self):
        input = """
s = "He said: OK
x = y + 1
"""
        expect = "\n,s,=,Unclosed String: He said: OK"
        self.assertTrue(TestLexer.test(input, expect, 179))

    def test_180(self):
        input = """
s = "He said: '"OK'""
x = y + 1
"""
        expect = """\n,s,=,He said: '"OK'",\n,x,=,y,+,1,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 180))

    def test_181(self):
        input = """ "He asked me: '"Where is John?'"" """
        expect = "He asked me: '\"Where is John?'\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))

    def test_182(self):
        input = """ s = "all legal escape: \\b \\f \\r \\n \\t \\' \\\\" """
        expect = """s,=,all legal escape: \\b \\f \\r \\n \\t \\' \\\\,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 182))

    def test_183(self):
        input = """
s = "an illegal escape: \\k"
a = 5
func main()
begin
    return 0
end
"""
        expect = """\n,s,=,Illegal Escape In String: an illegal escape: \\k"""
        self.assertTrue(TestLexer.test(input, expect, 183))

    def test_184(self):
        input = """
number a[5] <- [1, 2, 3, 4, 5]
number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
"""
        expect = """\n,number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],\n,number,b,[,2,,,3,],<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],],\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 184))

    def test_185(self):
        input = """
number a[5] <- [1, 2, 3, 4, 5]
number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
"""
        expect = """\n,number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],\n,number,b,[,2,,,3,],<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],],\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 185))

    def test_186(self):
        input = """
a[3 + foo(2)] <- a[b[2, 3]] + 4
"""
        expect = """\n,a,[,3,+,foo,(,2,),],<-,a,[,b,[,2,,,3,],],+,4,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 186))

    def test_187(self):
        input = """s = 'This is string'\""""
        expect = "s,=,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test_188(self):
        input = """
func foo(number a[5], string b)
begin
    var i <- 0
    for i until i >= 5 by 1
    begin
        a[i] <- i * i + 5
    end
    return -1
end
"""
        expect = """
,func,foo,(,number,a,[,5,],,,string,b,),
,begin,
,var,i,<-,0,
,for,i,until,i,>=,5,by,1,
,begin,
,a,[,i,],<-,i,*,i,+,5,
,end,
,return,-,1,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_189(self):
        input = """s = 'This is string'"""
        expect = "s,=,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test_190(self):
        input = """
begin
    number r
    number s
    r <- 2.0
    number a[5]
    number b[5]
    s <- r * r * 3.14
    a[0] <- s
end
"""
        expect = """
,begin,
,number,r,
,number,s,
,r,<-,2.0,
,number,a,[,5,],
,number,b,[,5,],
,s,<-,r,*,r,*,3.14,
,a,[,0,],<-,s,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_191(self):
        input = """
func areDivisors(number num1, number num2)
    return (num1 % num2 = 0 or num2 % num1 = 0)
func main()
    begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if areDivisors(num1, num2) printString("Yes")
        else printString("No")
    end
"""
        expect = """
,func,areDivisors,(,number,num1,,,number,num2,),
,return,(,num1,%,num2,=,0,or,num2,%,num1,=,0,),
,func,main,(,),
,begin,
,var,num1,<-,readNumber,(,),
,var,num2,<-,readNumber,(,),
,if,areDivisors,(,num1,,,num2,),printString,(,Yes,),
,else,printString,(,No,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_192(self):
        input = """
func isPrime(number x)
func main()
    begin
        number x <- readNumber()
        if isPrime(x) printString("Yes")
        else printString("No")
    end
    
func isPrime(number x)
    begin
        if x <= 1 return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
            if x % i = 0 return false
        end
        return true
    end
"""
        expect = """
,func,isPrime,(,number,x,),
,func,main,(,),
,begin,
,number,x,<-,readNumber,(,),
,if,isPrime,(,x,),printString,(,Yes,),
,else,printString,(,No,),
,end,
,
,func,isPrime,(,number,x,),
,begin,
,if,x,<=,1,return,false,
,var,i,<-,2,
,for,i,until,i,>,x,/,2,by,1,
,begin,
,if,x,%,i,=,0,return,false,
,end,
,return,true,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_193(self):
        input = """
func main()
begin
    ho = "Dang Duong Minh"
    ten = "Nhat"
    fullname = ho ... " " ... ten
    printString(fullname)
end
"""
        expect = """
,func,main,(,),
,begin,
,ho,=,Dang Duong Minh,
,ten,=,Nhat,
,fullname,=,ho,..., ,...,ten,
,printString,(,fullname,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_194(self):
        input = """\"abc
"""
        expect = "Unclosed String: abc"
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test_195(self):
        input = """
string a <- "abc ## this is a comment
"""
        expect = "\n,string,a,<-,Unclosed String: abc ## this is a comment"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_196(self):
        input = """\"abcdefghijklmn#^7182930&*()0#@!~}]{/.><-_+=!@#$%^&*().,;:|[]{}\""""
        expect = "abcdefghijklmn#^7182930&*()0#@!~}]{/.><-_+=!@#$%^&*().,;:|[]{},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test_197(self):
        input = """
"abcxyz\\r"
"""
        expect = """
,abcxyz\\r,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test_198(self):
        input = """
string a <- "abc'abc"
"""
        expect = """
,string,a,<-,abc'abc,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))

    def test_199(self):
        input = """string a <- "abc'\""""
        expect = "string,a,<-,Unclosed String: abc'\""
        self.assertTrue(TestLexer.test(input, expect, 199))
