'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from Visitor import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
import struct


def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("writeNumber", MType([NumberType()], VoidType()), CName(self.libName))]

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None


class SubBody():
    def __init__(self, frame, sym):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        # value: Int

        self.value = value


class CName(Val):
    def __init__(self, value):
        # value: String

        self.value = value


class Register:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Management:
    def __init__(self):
        self.register_name = ["$t0", "$t1", "$t2", "$f0", "$f1", "$f2", "$f12"]
        self.register_use = {}
        self.register = {}
        for name in self.register_name:
            self.register_use[name] = False
            self.register[name] = Register(name)

    def get_unused_register(self, prefix):
        for i in range(3):
            name = "$" + prefix + str(i)
            if self.register_use[name] == False:
                self.register_use[name] = True
                return self.register[name]

    def pop_register(self, name):
        self.register_use[name] = False

    def get_register(self, name):
        if self.register_use[name]:
            raise "Used register"
        self.register_use[name] = True
        return self.register[name]


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "ZCodeClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".asm")
        self.manage = Management()
        self.path_io = "./lib/io.asm"

    def visitProgram(self, ast, c):
        # ast: Program
        # c: Any
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, e)

        file = open(self.path_io)
        data = file.read()
        file.close()
        self.emit.printout(data)
        self.emit.emitEPILOG()
        return c

    def visitFuncDecl(self, ast, o):
        # ast: FuncDecl
        # o: Any

        # Just for main function because of assignment 2
        if ast.name.name == "main":
            self.emit.printout(self.emit.emitMETHOD(ast.name.name))
            if ast.body:
                self.visit(ast.body, o)
            self.emit.printout(self.emit.emitEXIT())
        else:
            pass

    def visitCallStmt(self, ast, o):
        # ast: FuncCall
        # o: Any
        # Just for writeNumber
        prog = ""
        for arg in ast.args:
            code, register = self.visit(arg, o)

            reg_12 = self.manage.get_register("$f12")
            prog += code + self.emit.emitMOV_S(reg_12, register)
            self.manage.pop_register(str(register))
        prog += self.emit.emitJAL(ast.name.name)
        return prog

    def visitBlock(self, ast, o):
        for stmt in ast.stmt:
            self.emit.printout(self.visit(stmt, o))

    def visitNumberLiteral(self, ast, o):
        # ast: NumberLiteral
        # o: Any

        code = ""
        reg_t = self.manage.get_unused_register("t")
        value = str(float_to_hex(ast.value))
        code += self.emit.emitLI(reg_t, value)

        reg_f = self.manage.get_unused_register("f")
        code += self.emit.emitMTC1(reg_t, reg_f)
        self.manage.pop_register(str(reg_t))
        return code, reg_f

    def visitBinaryOp(self, ast, o):
        frame = o.frame
        sym = o.sym

        lhs, reg_l = self.visit(ast.left, o)
        rhs, reg_r = self.visit(ast.right, o)

        code = lhs + rhs + self.emit.emitADD_S(reg_l, reg_l, reg_r)
        self.manage.pop_register(str(reg_r))

        return code, reg_l
