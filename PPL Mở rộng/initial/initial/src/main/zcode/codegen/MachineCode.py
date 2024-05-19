'''
*   @author Dr.Nguyen Hua Phung
*   @version 1.0
*   28/6/2006
*   This class provides facilities for method generation
*
'''
from abc import ABC, abstractmethod, ABCMeta


class MachineCode(ABC):

    @abstractmethod
    def emitADD_S(self, f0, f1, f3):
        pass

    @abstractmethod
    def emitLI(self, t1, num):
        pass

    @abstractmethod
    def emitMTC1(self, t1, f1):
        pass

    @abstractmethod
    def emitJAL(self, func):
        pass

    @abstractmethod
    def emitMETHOD(self, name):
        pass

    @abstractmethod
    def emitEXIT(self):
        pass

    @abstractmethod
    def emitMOV_S(self, f0, f1):
        pass

    @abstractmethod
    def emitINCLUDE(self, path):
        pass


class MipsCode(MachineCode):
    END = "\n"
    INDENT = "\t"

    def emitADD_S(self, f0, f1, f3):
        return MipsCode.INDENT + "add.s " + str(f0) + ", " + str(f1) + ", " + str(f3) + MipsCode.END

    def emitLI(self, t1, num):
        return MipsCode.INDENT + "li " + str(t1) + ", " + str(num) + MipsCode.END

    def emitMTC1(self, t1, f1):
        return MipsCode.INDENT + "mtc1 " + str(t1) + ", " + str(f1) + MipsCode.END

    def emitJAL(self, func):
        return MipsCode.INDENT + "jal " + str(func) + MipsCode.END

    def emitMETHOD(self, name):
        return str(name) + ":" + MipsCode.END

    def emitEXIT(self):
        return self.emitJAL("exit")

    def emitMOV_S(self, f0, f1):
        return MipsCode.INDENT + "mov.s " + str(f0) + ", " + str(f1) + MipsCode.END

    def emitINCLUDE(self, path):
        return ".include " + str(path) + MipsCode.END
