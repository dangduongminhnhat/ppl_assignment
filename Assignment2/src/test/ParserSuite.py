import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_200(self):
        """Simple program: int main() {} """
        input = input = """func main()
begin
## This is comment.
a <- 5
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_201(self):
        """Simple program: int main() {} """
        input = """func main()
begin
a <- "This is a string containing tab \\t"
b <- "He asked me: '"Where is John?'""
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        """Simple program: int main() {} """
        input = """func main()
begin
number a[5] <- [1, 2, 3, 4, 5]
number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        """Simple program: int main() {} """
        input = """func main()
begin
a[3 + foo(2)] <- a[b[2, 3]] + 4
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        """Simple program: int main() {} """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        """Simple program: int main() {} """
        input = """func foo(number a[5], string b)
begin
aPI <- 3.14
l[3] <- value * aPi
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        """Simple program: int main() {} """
        input = """func foo(number a[5], string b)
begin
aPI <- 3.14
l[3] <- value * aPi
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        """Simple program: int main() {} """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        """Simple program: int main() {} """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        """Simple program: int main() {} """
        input = """func isPrime(number x)
func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("Yes")
else writeString("No")
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210(self):
        """Simple program: int main() {} """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        """Simple program: int main() {} """
        input = """## this program has only two lines: this comment and the following function declaration.

func main() 
begin
writeString("Hello world")
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        """Simple program: int main() {} """
        input = """func main()
        begin
        string c <- "\mmmp"
        end
        """
        expect = "\\m"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_213(self):
        """Simple program: int main() {} """
        input = """func foo(number a[1,2,3])
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        """Simple program: int main() {} """
        input = """func main()
begin
number arr["string",abc()] <- [[1,2],[2,3]]
end
        """
        expect = "Error on line 3 col 11: string"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        """Simple program: int main() {} """
        input = """func main()
begin
number a[1,"abc",true] <- 1
end
        """
        expect = "Error on line 3 col 11: abc"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
        """Simple program: int main() {} """
        input = """func main() return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
        """Simple program: int main() {} """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        """Simple program: int main() {} """
        input = """func main()
begin
arr["BTL"] <- true

arr[0] <- b["PPL",2]

x <- "qua" + 3 

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_219(self):
        """Simple program: int main() {} """
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_220(self):
        """Simple program: int main() {} """
        input = """
s = "an illegal escape: \\k"
a = 5
func main()
begin
    return 0
end
"""
        expect = "Error on line 2 col 0: s"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        """Simple program: int main() {} """
        input = """func foo(number a) begin
if ((a=1) or (a=0)) return 1
return a*foo(a)
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(foo(3))]]

func main()
begin
number a<- arr[foo(1),foo(3)%3]*(-1
return
end
"""
        expect = """Error on line 10 col 35: 
"""
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        """Simple program: int main() {} """
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):
        """Simple program: int main() {} """
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
        expect = """Error on line 3 col 43: ="""
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):
        """Simple program: int main() {} """
        input = """func max(number a, string b)
begin 
if foo(boolean >= 4) 
doSomething(a,2,\"b\")


elif (abc > \"abc\")

doSomethingElif(b,true,foo(x,2))
end
"""
        expect = "Error on line 3 col 3: foo"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
        """Simple program: int main() {} """
        input = """
func main()
begin
    ho = "Dang Duong Minh"
    ten = "Nhat"
    fullname = ho ... " " ... ten
    printString(fullname)
end
"""
        expect = """Error on line 4 col 7: ="""
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):
        """Simple program: int main() {} """
        input = """
string a <- "abc ## this is a comment
"""
        expect = """abc ## this is a comment"""
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
        """Simple program: int main() {} """
        input = """
string a <- "abc'abc"
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        """Simple program: int main() {} """
        input = """ 
            number DangNhat
            
            ## DangNhat
            number DangNhat <- 0
            bool a[122,15]
            bool a[122,15] <- 1 + 1 / 2 * 3
            string b[3]
            ## 12 
            
            string b[3] <- 2 ... " tring"
            var i <- 0
            dynamic i
            dynamic i <- 0
            ## DangNhat
             
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_229(self):
        input = """ 
            var MiNhat
        """
        expect = "Error on line 2 col 22: \n"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_230(self):
        input = """ 
            dynamic MiNhat[5] <- 3
        """
        expect = "Error on line 2 col 26: ["
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_231(self):
        input = """ 
            bool a["string"]
            bool a[[1,2]]
            bool a[1+1]
        """
        expect = "Error on line 2 col 19: string"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_232(self):
        input = """ 
            bool a[1,]
        """
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_233(self):
        input = """ 
            var a[1]
        """
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        input = """ 
            func main()
            func main(number f1)
            func main(number a[5],bool x[5,2,3], bool a[5,2,3], string b, bool c)
            func main(number num1, number num2)
                var MiNhat <- 1
            func main(number f1 <- c)
        """
        expect = "Error on line 7 col 32: <-"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_235(self):
        input = """ 
            func main()
            ## Dang Nhat
            func main() func main(dynamic a) ## Dang Nhat
        """
        expect = "Error on line 4 col 24: func"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        input = """ 
            func main(var a)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        input = """ 
            ##12
            ##12
            
            func main(number a) var c <- 1
        """
        expect = "Error on line 5 col 32: var"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_238(self):
        input = """ 
            func main(string a) 
                begin 
                    break ## 12
                end
            func main(dynamic a) 
        """
        expect = "Error on line 6 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        input = """ 
            func main(number a[1,2,3]) ##12
                break
        """
        expect = "Error on line 3 col 16: break"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        input = """ 
            ##12
            func main(number a) 
                ##12
                
                begin 
                    break
                end
                
                ##12
                ##12
            func main(number a)
            ##12        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
        input = """ 
            ## 12
            
            var a <- 1 ## 12
            ## 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_242(self):
        input = """var a <- 1"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_243(self):
        input = """func main(number a) """
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_244(self):
        input = """ var MiNhat <- "Mi" ... "Nhat" 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_245(self):
        input = """ var MiNhat <- "Mi" ... 1 ... "Nhat" 
        """
        expect = "Error on line 1 col 26: ..."
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_246(self):
        input = """ 
            var MiNhat <- true > "true" 
            var Minhat <- true >= "true"
            var MiNhat <- true = "true"
            var MiNhat <- true == "true"
            var MiNhat <- true < "true"
            var MiNhat <- true <= "true"
            var MiNhat <- true >= "true" ... 1 > 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_247(self):
        input = """ var MiNhat <- true > x >= z 
        """
        expect = "Error on line 1 col 24: >="
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_248(self):
        input = """ 
            var MiNhat <- true and "true" or 1 
            var MiNhat <- 1 and 2 and 3 or 4 or 4
            var MiNhat <- 1 + 2 - 2 + 3 and 3
            var MiNhat <- 1 / 2 * 3 % 4
            var MiNhat <- 1 / 2 / 2 * 3 % 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_249(self):
        input = """var MiNhat <- true >= "true" and 1 > 2
        """
        expect = "Error on line 1 col 35: >"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_250(self):
        input = """ 
            var MiNhat <- -1 * not 1
            var MiNhat <- not not not----C
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_251(self):
        input = """var MiNhat <- - not 1
        """
        expect = "Error on line 1 col 16: not"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_252(self):
        input = """ 
            var MiNhat <- a[1] + 1
            var MiNhat <- array[1,1+2][1][2,3]
            var MiNhat <- array[1,(1)...2,array[ar[(1*2) and 1]],array[2]]
            var MiNhat <- a[1] + fun()[1,fun()] 
            var MiNhat <- 1[1]
        """
        expect = "Error on line 3 col 38: ["
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_253(self):
        input = """var MiNhat <- a[]
        """
        expect = "Error on line 1 col 16: ]"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_254(self):
        input = """ 
            var MiNhat <- a()
            var MiNhat <- a(1,2)
            var MiNhat <- a(x,array[2])[2]
            var MiNhat <- a(z,k[3] ... 2)[1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_255(self):
        input = """var MiNhat <- a()()
        """
        expect = "Error on line 1 col 17: ("
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_256(self):
        input = """ 
            var MiNhat <- a() + ++1 / 2 *3 <= 3 ... "v" >= 2
            var MiNhat <- a(1,2)[1,2,3 ... 2] + false + true
            var MiNhat <- a(z,k[2,3,"2"] ... 2)[true]
            var MiNhat <- (a ... 3) ... b and (a >= b) < b[1, b[1]]
            var MiNhat <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
            var MiNhat <- a(x,array[2])[2,3+2,true,false]
        """
        expect = "Error on line 2 col 32: +"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_257(self):
        input = """var MiNhat <- a[1]()
        """
        expect = "Error on line 1 col 18: ("
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_258(self):
        input = """
        ## comment
        func main()

            ## comment
            begin
            aPI <- 3.14
            end
            ## comment
            
        ## comment
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_259(self):
        input = """
        func main() begin 
        end
        func main() 
            begin 
                ## comment0
            end
        func main()
            ## comment1
            begin
                ## comment2
                
                ## comment3
                MiNhat <- 1 + 2 + fun()
                MiNhat[1+a] <- 1
                
                ## comment4
                MiNhat[3+4,2,4] <- 1
                
                ## comment5
            end
            ## comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_260(self):
        input = """
        func main()
            begin
            aPI + 1 <- 3.14
            end
        """
        expect = "Error on line 4 col 16: +"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_261(self):
        input = """
        func main()
            begin
            aPI()<- 3.14
            end
        """
        expect = "Error on line 4 col 17: <-"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_262(self):
        input = """
        func main()
            begin
            (aPI)[2]<- 3.14
            end
        """
        expect = "Error on line 4 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_263(self):
        input = """
        func main()
            begin   
                if(1+1) api <- 1
                ## comment0
                
                if(1+1) 
                    ## comment1
                    
                    api <- 1
                    ## comment2
                else api <- 1
                ## comment3
                
                if (1) api <- 1
                elif (1 ... 2)
                    ## comment1
                    
                    api <- 1
                    ## comment2
                elif (1) api <- 1
                
                if (1) api <- 1
                elif (1 ... 2) api <- 1
                elif (1) api <- 1
                else api <- 1   
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_264(self):
        input = """
        func main()
            begin   
                if (api <- 1)
            end
        """
        expect = "Error on line 4 col 24: <-"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_265(self):
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
                ## comment
                
                a <- 1
            ## comment
            end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_266(self):
        input = """
        func main()
            begin
            for i[1] until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_267(self):
        input = """
        func main()
            begin
            for i+1 until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_268(self):
        input = """
        func main()
        begin 
            break
            continue
            for i until i >= 10 by 1 + 1 ... 3 / 2
                begin
                    break
                    continue
                end
                
            for i until i >= 10 by 1 print(1)
            for i until i >= 10 by 1 
                print(1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_269(self):
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_270(self):
        input = """
        func main()
            return 1 + 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_271(self):
        input = """
        func main()
            begin
            main()
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_272(self):
        input = """
        func main()
        begin 
            return ([1,2,3]) + 1
            return main()
            main(1,2)
            fun()
            main([1,2,3], 1+2, a, c ... e)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_273(self):
        input = """
        func main()
            return func()
        """
        expect = "Error on line 3 col 19: func"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_274(self):
        input = """
        func main()
            return break
        """
        expect = "Error on line 3 col 19: break"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_275(self):
        input = """
        func main()
            begin
                begin
                    begin
                        x <- 1
                    end
                    
                    begin
                        return true
                    end
                    
                    return false
                end
                
                begin
                end
                return true
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_276(self):
        input = """var aPI <- 3.14"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_277(self):
        input = """
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_278(self):
        input = """
            func isPrime(number x)
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end
            func isPrime(number x)
            begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
            if (x % i = 0) return false
            end
            return true
            
            
            for i until i > x / 2 by 1 + 1 var c <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_279(self):
        self.assertTrue(TestParser.test(
            "", "Error on line 1 col 0: <EOF>", 279))

    def test_280(self):
        input = """number a[1] <- ["hihi"]
                bool ahihi[10,23] <- [a[b[2, 3]] + 4]
                string ahihi[2] <- [[1,2,3],[2,1,2]]
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_281(self):
        input = """a<-10
            """
        expect = "Error on line 1 col 0: a"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_282(self):  # check output
        input = """number a <- 10"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        input = """func main(number b, string b, number a[5]) return 2
            number a
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        input = """var tRue <- true
        func ahihi() return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        input = """
        var tRue <- true
        func ahihi() return
        if (IF) else fALse <- true
        """
        expect = "Error on line 4 col 8: if"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        input = """
        var tRue <- true
        func ahihi() begin 
        return
        if (IF) else fALse <- true
        end
        """
        expect = "Error on line 5 col 16: else"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = """
        var 1a <- 10
        """
        expect = "Error on line 2 col 12: 1"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = """
        var true <- 10
        """
        expect = "Error on line 2 col 12: true"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        input = """
        var fAlse <- (10.89e-1*8..."ahihi")%7
        """
        expect = "."
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        input = """
        var fAlse <- (10.89e-1*8.0e1-9...."ahihi")%7.
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = """
        var a <- []
        """
        expect = "Error on line 2 col 18: ]"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = """func main() return
        return
        """
        expect = 'Error on line 2 col 8: return'
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = """func main() return
        var a = []
        """
        expect = 'Error on line 2 col 14: ='
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = """boolean isTrue <- true()
        """
        expect = 'Error on line 1 col 0: boolean'
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = """bool isTrue <- true()
        """
        expect = 'Error on line 1 col 19: ('
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = """bool isValid <- true and false
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = """average <- (score1 + score2) / 2"""
        expect = """Error on line 1 col 0: average"""
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = """string stringWith <- "test inside: \"Hello\"\""""
        expect = """Error on line 1 col 36: Hello"""
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = """func main() begin
        foo()[1] <- 1
        end
        """
        expect = """Error on line 2 col 13: ["""
        self.assertTrue(TestParser.test(input, expect, 299))
