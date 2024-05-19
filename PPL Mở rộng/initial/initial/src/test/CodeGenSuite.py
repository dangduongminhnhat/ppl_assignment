import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_500(self):
        input = """func main ()
        begin
            writeNumber(1.0 + 1.0)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_501(self):
        input = """func main ()
        begin
            writeNumber(1 + 2)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_502(self):
        input = """func main ()
        begin
            writeNumber(1 + 2.0 + 3 + 4.0 + 5.0)
        end
        """
        expect = "15.0"
        self.assertTrue(TestCodeGen.test(input, expect, 502))
