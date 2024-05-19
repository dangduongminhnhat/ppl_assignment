from Utils import *
from StaticCheck import *
from StaticError import *
import CodeGenerator as cgen
from MachineCode import MipsCode


class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.mips = MipsCode()

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''

    def printout(self, in_):
        # in_: String

        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()

    def emitMETHOD(self, name):
        return self.mips.emitMETHOD(name)

    def emitEXIT(self):
        return self.mips.emitEXIT()

    def emitMTC1(self, t1, f1):
        return self.mips.emitMTC1(t1, f1)

    def emitLI(self, t1, num):
        return self.mips.emitLI(t1, num)

    def emitADD_S(self, f0, f1, f3):
        return self.mips.emitADD_S(f0, f1, f3)

    def emitJAL(self, func):
        return self.mips.emitJAL(func)

    def emitMOV_S(self, f0, f1):
        return self.mips.emitMOV_S(f0, f1)

    def emitINCLUDE(self, path):
        return self.mips.emitINCLUDE(path)
