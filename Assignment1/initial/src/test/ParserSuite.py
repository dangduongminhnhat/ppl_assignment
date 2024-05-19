import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    parserTest = 199

    def test_parser_00(self):
        inp = \
            """func main () return 1
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_01(self):
        inp = \
            """func _main_() begin
end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_02(self):
        inp = \
            """## Helper function
func getVar(number x, bool b0)
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_03(self):
        inp = \
            """func getVar(number x, bool b0)
begin
    var a <- "abc\\nt."..."67+\\t12"
    var b <- (true and b0) or a == "315" and b0 >= 7
    return a
end
"""
        out = "Error on line 4 col 48: >="
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_04(self):
        inp = \
            """

var const <- 4 ## declare variable
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_05(self):
        inp = \
            """func main()  
    begin
        var x <- const* (4 + -12)
    x <- 7 and 1
number arr[3] <- [const,n[8],  getVar(6,true)]

end


"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_06(self):
        inp = \
            """

func main(var x, number y)  
begin
end
"""
        out = "Error on line 3 col 10: var"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_07(self):
        inp = \
            """\tbegin
end
"""
        out = "Error on line 1 col 1: begin"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_08(self):
        inp = \
            """func main(string x, number y)  
begin
end"""
        out = "Error on line 3 col 3: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_09(self):
        inp = \
            """
"""
        out = "Error on line 2 col 0: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_10(self):
        inp = """"""
        out = "Error on line 1 col 0: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_11(self):
        inp = \
            """func func(string str)
begin
    writeString(str)    
end
"""
        out = "Error on line 1 col 5: func"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_12(self):
        inp = \
            """func foo(string str)
writeString(str)
var x <- 7 + (t - false)
end
"""
        out = "Error on line 2 col 0: writeString"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_13(self):
        inp = \
            """func foo(string str) begin
begin
writeString(str)
end
"""
        out = "Error on line 5 col 0: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_14(self):
        inp = \
            """func foo(string str)
begin
writeString(str)
"""
        out = "Error on line 4 col 0: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_15(self):
        inp = \
            """func foo(string str)
var x <- 7 + (t - false)
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_16(self):
        inp = \
            """func foo(string str)
var x <- 7 + (t - false)
writeString(str)
"""
        out = "Error on line 3 col 0: writeString"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_16(self):
        inp = \
            """func foo()
var x <- 7 + (t - false)
begin
writeString(str)
end
"""
        out = "Error on line 3 col 0: begin"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_17(self):
        inp = \
            """func return(bool b)
begin
x <- 6 +
end
"""
        out = "Error on line 1 col 5: return"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_18(self):
        inp = \
            """func key(bool b)
begin
x <- 6 +
end
"""
        out = "Error on line 3 col 8: \n"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_19(self):
        inp = \
            """func key(bool b)
begin
boolean b <- false
return b and b
end
"""
        out = "Error on line 3 col 8: b"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_20(self):
        inp = \
            """func key(boolean b)
begin
bool b <- 7
return b and b
end
"""
        out = "Error on line 1 col 9: boolean"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_21(self):
        inp = \
            """func foo(number num)

func bar(number x <- 6)
begin ## begin
var x <- x + 6
end
"""
        out = "Error on line 3 col 18: <-"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_22(self):
        inp = \
            """func foo(number num)

func bar(number x[2])
begin ## begin
var x <- y + \"abc\"
end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_23(self):
        inp = \
            """func foo(number num)

func bar(string str)   

begin ## begin
var x <- y + \"abc\"
end

var y
"""
        out = "Error on line 9 col 5: \n"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_24(self):
        inp = \
            """func foo(number num)

func bar(string str)   

begin ## begin
var x <- y + \"abc\"
end

dynamic y
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_25(self):
        inp = \
            """func foo(number num)

func bar(string str)   
begin ## begin
dynamic x <- y + \"abc\0\"
end

number y
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_26(self):
        inp = \
            """func bar(string str)   
begin ## begin
var x <- y + \"abc\\'x\"
end

number arr[7]
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_27(self):
        inp = \
            """func bar(string str[6])   
begin ## begin
var x <- y + \"abc'\"x\"
end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_28(self):
        inp = \
            """func bar(string str)   
begin ## begin
var x <- y + \"abc\\'x\"
end

number arr[true]
"""
        out = "Error on line 6 col 11: true"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_29(self):
        inp = \
            """func bar(string str) ## func ##
begin
var x <- y + \"abc\\'x\"
end

number arr[\"6\"]
"""
        out = "Error on line 6 col 11: 6"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_30(self):
        inp = \
            """func bar(string str[false]) ## func ##
begin
var x <- y + \"abc\\'x\"
end

number arr[true]
"""
        out = "Error on line 1 col 20: false"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_31(self):
        inp = \
            """func bar(string str[2] <- [2,3,6])
begin
var x <- y + \"abc\\'x\"
end

number arr[true]
"""
        out = "Error on line 1 col 23: <-"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_32(self):
        inp = \
            """func bar(bool str[6*2])
## begin
var x <- y + \"abc\\'x\"
end

number arr[true]
"""
        out = "Error on line 1 col 19: *"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_33(self):
        inp = \
            """func bar(number arr[6,8])
begin
## number arr[6,8]
x[6,8] <- y + \"abc\\'x\"...6
## end

number arr[true]
"""
        out = "Error on line 7 col 11: true"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_34(self):
        inp = \
            """func bar(number arr[6,8])
begin
x[2,8] <- y + \"abc\\'x\"...6
end

"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_35(self):
        inp = \
            """func bar(number arr, bool b)
begin
x[2,8] <- [1,2,3]
end

"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_35(self):
        inp = \
            """func bar(number arr[6,8], bool r)
begin
x[2,8] <- [1,2,"3"]
end

"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_36(self):
        inp = \
            """func bar(number arr[6,8], bool)
begin
x[2,8] <- [1,2,\"3\"], [4,\"5\",6] 
end

"""
        out = "Error on line 1 col 30: )"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_37(self):
        inp = \
            """func bar(number arr,)
begin
x[2,8] <- [1,2,\"3\"], [4,\"5\",6] 
end

"""
        out = "Error on line 1 col 20: )"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_38(self):
        inp = \
            """func bar(number    arr)
begin
x[2,8] <- [1,2,\"3\"], [4,\"5\",6] 
end

"""
        out = "Error on line 3 col 19: ,"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_39(self):
        inp = \
            """func bar(    number\tarr)
begin
x[2,8] <- [[1,2,\"3\"], [4,\"5\",6] ]
end

"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_40(self):
        inp = \
            """func bar(number arr,,)
begin
x[2,8] <- [1,2,\"3\"] + [4,\"5\",6]
end

"""
        out = "Error on line 1 col 20: ,"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_41(self):
        inp = \
            """func bar(number arr,bool b   
, string str)
begin
x[2,8] <- [1,2,\"3\"] + [4,\"5\",6]
end

"""
        out = "Error on line 1 col 29: \n"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_42(self):
        inp = \
            """func bar(number arr,bool b   ,
string str)
begin
x[2,8] <- [1,2,\"3\"] + [4,\"5\",6]
end

"""
        out = "Error on line 1 col 30: \n"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_43(self):
        inp = \
            """func bar(number arr,bool b ) begin
begin
x[2,8] <- [1,2,\"3\"] + [4,\"5\",[6,5]]
end
end

"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_44(self):
        inp = \
            """func bar(number arr,bool b ) begin end
begin
x[2,8] <- [1,2,\"3\"] + [4,\"5\",6]
end

"""
        out = "Error on line 1 col 35: end"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_45(self):
        inp = \
            """func bar
(number arr,bool b )
begin
x[2,8] <- [1,2,\"3\",]
end

"""
        out = "Error on line 1 col 8: \n"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_46(self):
        inp = \
            """func bar(number arr,bool b )
begin
x[2,8] <- [1,2,\"3\",154/4]
var x
end

"""
        out = "Error on line 4 col 5: \n"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_47(self):
        inp = \
            """func bar(number arr,bool b )
begin
x[2,8] <- [1,2,\"3\",154/4]
var x <- [1,3.4]
end"""
        out = "Error on line 5 col 3: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_48(self):
        inp = \
            """func bar(number arr,bool b )
begin
x[2,1e9] <- [1,2,\"ab\ncd\",154/4]
var x <- readString(\"abc\")
end
"""
        out = "ab"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_49(self):
        inp = \
            """func bar(number arr,bool b )
begin
x[2,8] <- foo([1,2,\"abcd\",154/4])
number x <- readString()
var x[6] <- [1,2,3] 
end
"""
        out = "Error on line 5 col 5: ["
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_50(self):
        inp = \
            """func bar(number arr,bool b )
begin
x[2,8] <- foo([1,2,\"ab\\cd\",154/4])
number x <- readString()
var x[6] <- [1,2,3] 
end
"""
        out = "ab\\c"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_51(self):
        inp = \
            """func bar(number arr,bool b )
begin
x[2,8] <- foo([1,2,\"abcd\",154/4])
number x <- readString()
number x[6] <- [1,2,3]
## Comment


end

## Day la comment ben ngoai
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_52(self):
        inp = \
            """func bar(number arr,bool b )
begin
x[2,8] <- foo([1,2,\"abcd\",154/4])
number x <- readString()
number x[6] <- [1,2,3]
## Comment


end

## Day la comment ben ngoai"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_53(self):
        inp = \
            """func bar(number arr,bool b )
begin
x[2,8] <- foo([1,2,\"abcd\",154/4])
number x <- readString(i)
number x[6] <- [1,2,3]
    ## Comment
return 

end ## Day la comment ben ngoai"""
        out = "Error on line 9 col 31: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_54(self):
        inp = \
            """##func max(number a, number b)
## begin
## Comment 1
##if (x <- 6) else doSomething()
## Comment 2
##end"""
        out = "Error on line 6 col 5: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_55(self):
        inp = \
            """func max(number a, string b)
begin
## Comment 
if (boolean) doSomething()
else 

doSomethingElse()
end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_56(self):
        inp = \
            """func max(number a, string b)
begin 
if foo(boolean >= 4) 
doSomething(a,2,\"b\")


elif (abc > \"abc\")

doSomethingElif(b,true,foo(x,2))
end
"""
        out = "Error on line 3 col 3: foo"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_57(self):
        inp = \
            """func min(number a, string b)
begin  
if (boolean) 
doSomething(a,2,\"b\")


elif (abc > \"abc\") doSomethingElif(b,true,foo(x,2))

else doSomethingElse(doSomethingElse,foo[3.2,3])
end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_58(self):
        inp = \
            """func min(number a, string b)
begin  
if (x <= false)
begin 
main(a,2,\"b\")
end

elif (abc > \"abc\") for id until id >= 4 by 1 loop(arr[a(b),b(a)])

return id
end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_59(self):
        inp = \
            """func min(number a, string b)
begin  
if (x <= false)
begin 
main(a,2,\"b\")
end

elif (abc > \"abc\") 

for id until id >= 4 by 1 loop1(arr[a(b),b(a)])
loop2(arr[a(b)],b[2])

func1(x) func2(y)
end
"""
        out = "Error on line 13 col 9: func2"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_60(self):
        inp = \
            """func min(number a, string b)
begin  
if (x <= false)
begin 
main(a,2,\"b\")
end
x <- 8*8
elif (abc > \"abc\") 

for id until id >= 4 by 1 loop1(arr[a(b),b(a)])
loop2(arr[a(b)],b[2])

func1(x) func2(y)
end
"""
        out = "Error on line 8 col 0: elif"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_61(self):
        inp = \
            """func min(number a, string b)
begin  
if (x <= false)
begin 
    main(a,2,\"b\")
end
x <- 8*8
else (abc > \"abc\") 

for id until id >= 4 by 1 loop1(arr[a(b),b(a)])
loop2(arr[a(b)],b[2])

func1(x) func2(y)
end
"""
        out = "Error on line 8 col 0: else"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_62(self):
        inp = \
            """func min(number a, string b)
begin  
if (x <= false)
    begin 
        main(a,2,\"b\")
    end
else (abc > \"abc\") 
    for id until id >= 4 by 1 


        loop1(arr[a(b),b(a)])
        loop2(arr[a(b)],b[2])

end
"""
        out = "Error on line 7 col 5: ("
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_63(self):
        inp = \
            """func min(number a, string b)
begin  
if (x <= false)
    begin 
        main(a,2,\"b\")
    end
for id until id >= 4 by 1 


    loop1(arr[a(b),b(a)])

    loop2(arr[a(b)],b[2])

end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_63(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for id until id >= 4 by 1 
x <- x + 1
end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_64(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for id until id >= 4 by 1 
return if
end
"""
        out = "Error on line 6 col 7: if"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_65(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for id until id >= 4 by 1 
return
end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_66(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for 1 until id >= 4 by 1 
if (x <= false) begin 
        writeBool(xyz)
    end
end
"""
        out = "Error on line 5 col 4: 1"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_67(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for i until true by \"abc\" 
if (x <= false) begin 
        writeBool()
    end
end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_68(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for i until true by \"abc\" 
if (x <= false) begin readBool()
    end
end
"""
        out = "Error on line 6 col 22: readBool"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_69(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
        readBool()
for foo(x) until true by \"abc\" 
if (x <= false) begin 
    end
end
"""
        out = "Error on line 6 col 7: ("
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_70(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for i+2 until true by \"abc\" 
if (1) begin 
    end
    func x(bool str) begin

    ok() end
end
"""
        out = "Error on line 5 col 5: +"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_71(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for 3+i until true by \"abc\" 
if (1) begin 
    end
    func x(bool str) begin

    ok() end
end
"""
        out = "Error on line 5 col 4: 3"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_72(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for index until index * 2 by \"abc\" 
if (1) begin 
    end
    func x(bool str) begin

    ok() end
end
"""
        out = "Error on line 8 col 4: func"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_73(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for index until index * 2 by \"abc\" 
if (1) begin 
    end
    x(bool str) begin

    ok() end
end
"""
        out = "Error on line 8 col 6: bool"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_74(self):
        inp = \
            """func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for index until index * 2 by \"abc\" 
if (1) begin   
    end
    x(boolean str) begin

    ok() end
end
"""
        out = "Error on line 8 col 14: str"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_75(self):
        inp = \
            """func min(number, string) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for index until index * 2 by \"abc\" 
if (1) begin   
    end
    x(boolean,) begin

    ok() end
end
"""
        out = "Error on line 1 col 15: ,"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_76(self):
        inp = \
            """func min(number x) begin       
if (x <= false) begin 
        foo(a,2,\"b\")
    end
for index until index * 2 by \"abc\" 
if (1) begin   
    end
    x(boolean,) begin

    ok() 
    end
end
"""
        out = "Error on line 8 col 14: )"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_77(self):
        inp = \
            """func min(number _) begin       
if (x <= _) begin 
        foo(a,2,\"b\")
    end
for index until index * 2 by \"abc\" 
if (1) begin   
    end
    _(boolean,_) begin

    _() 
    end
end
"""
        out = "Error on line 8 col 17: begin"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_78(self):
        inp = \
            """func min(number _) begin       
if (x <= _) begin 
        foo(a,2,\"b\")
    end
for index until index * 2 by \"abc\" 
if (1) begin   
    end
    _(boolean,_) 
    begin

    _(___,__,_____ ) 
    __ <- ____ * _ + __ - _(__,___)[_,__,____]
end
"""
        out = "Error on line 14 col 0: <EOF>"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_79(self):
        inp = \
            """func min(number _) begin       
if (x <= _) begin 
        foo(a,2,\"b\",[2,31,1])
    end
for index until index * 2 by \"abc\" 
if (var x + 2) begin   
    end
    _(boolean,_) 
    begin

    _(___,__,_____ ) 
    __ <- ____ * _ + __ - _(__,___)[_,[__,8],____]
end
"""
        out = "Error on line 6 col 4: var"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_80(self):
        inp = \
            """func far(number _) begin       
if (x <= _) begin 
        foo(a,2,\"b\")
    end
for index until index * 2 by \"abc\" 
if (_) begin   
    end
    _(boolean,_) 
    begin

    _(___,__,_____ ) 
    __ <- ____ * _ + __ - _(__,___)[_,[__,8],____]
end
end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_80(self):
        inp = \
            """func True(number _) begin       
if (x <= _ and f(z) == true or _) 
        falSe(a,2,\"b\")

end
"""
        out = "Error on line 2 col 20: =="
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_81(self):
        inp = \
            """func True(number _) begin       
if ((x <= _ and f(z)) == true or _) if (xy == yx...\"\") xy <- xy
        else falSe(a,2,\"b\")
        return True(true) + i*falSe[12,\"34\"]

end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_82(self):
        inp = \
            """func True(number _) begin       
if ((x <= _ and f(z)) == true or _) if (xy == yx...\"\") xy <- xy
        else falSe(a,2,\"b\")
        return True(true) + i*falSe[12,\"34\"]

end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_83(self):
        inp = \
            """func True(number _) begin       
if ((x <= _ and f(z)) == true or _) if (xy == yx...\"\") xy <- xy
        else falSe(a,2,\"b\")
        foo(x)[5] <- 7
        return True(true) + i*falSe[12,\"34\"]

end
"""
        out = "Error on line 4 col 14: ["
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_84(self):
        inp = \
            """func True(number _) begin       
if ((x <= _ and f(z)) == true or _) if (xy == yx...\"\") xy <- xy
        else falSe(a,2,\"b\")
        foo[5] <- foo()[7] + 7
        return True(true) + i*falSe[12,\"34\",[2]]

end
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_85(self):
        inp = \
            """
func returN(bool rEturn)
return


func True(number _) begin       
if ((x <= _ and f(z)) == true or _) if (xy == yx...\"\") xy <- xy
        else falSe(a,2,\"b\")
        foo[5] <- foo(x)[7,[1,[2,[3,[4,1+6 - false,\"\\n\"]]]]] + 7
        return True(true) + i*falSe[12,\"34\",[2]]

end
## something"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_86(self):
        inp = \
            """
func returN(bool rEturn)
return


func True(number _) begin       
if ((x <= _ and f(z)) == true or _) if (xy == yx...\"\") xy <- xy
        else falSe(a,2,\"b\")
        foo <- foo[7,[1,[2,[3,[4,5,\"\\n\"],[]]]]] + 7
        return True(true) + i*falSe[]

end
"""
        out = "Error on line 9 col 42: ]"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_87(self):
        inp = \
            """
func returN(bool rEturn)
return


func True(number _) begin       
if (((x <= _ and f(z))) == true or _) if (xy == yx...\"\") xy <- xy
        else falSe(a,2,\"b\")
        foo <- f[[[61]]] + []
        return True(true) + i*falSe[]

end
"""
        out = "Error on line 9 col 28: ]"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_88(self):
        inp = \
            """
func returN(bool rEturn)
return


func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([2,3] == yx...\"\") xy <- xy
        else falSe(a,2,\"b\")
        var foo <- f[[[61,1,3],4],[7+8]] + arr[3][5]
        return True(true) + i*falSe[]

end
"""
        out = "Error on line 9 col 49: ["
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_89(self):
        inp = \
            """func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([2,3] == yx...\"\") xy <- xy
        else falSe(a,2,\"b\")
        var foo <- f[[[61,1,3],4],[7+8]] + arr[3][5]
        return True(true) + i*falSe[]

end
"""
        out = "Error on line 4 col 49: ["
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_90(self):
        inp = \
            """func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([2,  3] ==yx...\"\") 

xy<-    xy
        else falSe(a,2,\"b\")
        var foo <- (begin
        foo()
        end)
        return True(true) + i*falSe[]

end
"""
        out = "Error on line 6 col 20: begin"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_91(self):
        inp = \
            """func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([2,  3] ==yx...\"\") 

xy<-    xy
        else falSe(a,2,\"b\")
        var foo <- (54 + 1)*(4 / true
        return True(true) + i*falSe[]

end
"""
        out = "Error on line 6 col 37: \n"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_92(self):
        inp = \
            """func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([2,  3] ==yx...\"\") 

xy<-    xy
        else falSe(a,-2,\"b\")
        var foo <- (54 + 1)*(4 / true[6,2)
        return True(true) + i*falSe[]

end
"""
        out = "Error on line 6 col 37: ["
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_93(self):
        inp = \
            """x <- 1

func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([2,  3] ==yx...\"\") 

xy<-    xy
        else falSe(a,2,\"b\")
        var foo <- (54 + 1)*(4 / true[6,2)
        return True(true) + i*falSe[]

end 
## something"""
        out = "Error on line 1 col 0: x"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_94(self):
        inp = \
            """number x <- 1

func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([2,  3] ==yx...\"\") 

xy<-    xy
        else falSe(a,2,\"b\")
        var foo <- (54 + 1)*(4 / True[6,2])
        arr[1+2]
        return True(true) + i*falSe[]

end 
"""
        out = "Error on line 9 col 16: \n"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_95(self):
        inp = \
            """number x <- 1
func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([-2,  3] ==yx...\"\") 

xy<-    xy
        else falSe(a,2,\"b\")
        var foo <- (54 + 1)*(4 / True[6,2])
        bool arr[-1] <- 7 
        return True(true) + i*falSe[]

end 
"""
        out = "Error on line 8 col 17: -"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_96(self):
        inp = \
            """number x <- 1
func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([-2,  3] ==yx...\"\") 

xy<-    xy
        else falSe(a,2,\"b\")
        var foo <- (54 + 1)*(4 / True[6,2])
        bool arr <- arr[-7] 
        return True(true) + i*falSe[6]

end 
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_97(self):
        inp = \
            """number x <- 1
func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([-2,  3] ==yx...\"\") 

xy<-    xy
        elif (1 + 2 == 3) return 0
        else if ( a- n < 6) number c
        var foo <- (54 + 1)*(4 / True[6,2])
        bool arr <- arr[-7] 
        return not -1

end 
"""
        out = "successful"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_98(self):
        inp = \
            """number x <- 1
func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([-2,  3] ==yx...\"...\") 

xy<-    xy
        else if ( a- n < 6) number c

        var foo <- (54 + 1)*(4 / true)[3]
        bool arr <- arr[-7]
        return not -1

end

"""
        out = "Error on line 8 col 38: ["
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))

    def test_parser_99(self):
        inp = \
            """func foo(number a) begin
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
        out = "Error on line 10 col 35: \n"
        ParserSuite.parserTest += 1
        self.assertTrue(TestParser.test(inp, out, ParserSuite.parserTest))
