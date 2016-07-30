import functools
from utils import is_64bit, Singleton
import pluginsdk._scriptapi
from pluginsdk.bridgemain import GuiUpdateAllViews


X86_DEBUG_REGISTERS = (
    'DR0', 'DR1', 'DR2', 'DR3', 'DR6', 'DR7'
)
X86_REGISTERS = (
    'EAX', 'AX', 'AH', 'AL',
    'EBX', 'BX', 'BH', 'BL',
    'ECX', 'CX', 'CH', 'CL',
    'EDX', 'DX', 'DH', 'DL',
    'EDI', 'DI', 'ESI', 'SI',
    'EBP', 'BP', 'ESP', 'SP',
    'EIP',
) + X86_DEBUG_REGISTERS

X64_REGISTERS = (
    'RAX', 'RBX', 'RCX', 'RDX',
    'RSI', 'SIL', 'RDI', 'DIL',
    'RBP', 'BPL', 'RSP', 'SPL', 'RIP',
    'R8', 'R8D', 'R8W', 'R8B',
    'R9', 'R9D', 'R9W', 'R9B',
    'R10', 'R10D', 'R10W', 'R10B',
    'R11', 'R11D', 'R11W', 'R11B',
    'R12', 'R12D', 'R12W', 'R12B',
    'R13', 'R13D', 'R13W', 'R13B',
    'R14', 'R14D', 'R14W', 'R14B',
    'R15', 'R15D', 'R15W', 'R15B',
) + X86_REGISTERS

GEN_REGISTERS = (
    'CIP',  # Generic EIP/RIP register
    'CSP'   # Generic ESP/RSP register
)

REGISTERS = (X64_REGISTERS if is_64bit() else X86_REGISTERS) + GEN_REGISTERS


class Register(object):
    __metaclass__ = Singleton

    def __init__(self, refresh_gui=True):
        self.refresh_gui = refresh_gui

        for register in REGISTERS:
            setattr(self.__class__, register, property(
                fget=functools.partial(self._get_func, register=register),
                fset=functools.partial(self._set_func, register=register)
            ))

    @staticmethod
    def __get_reg_function(register, get=True):
        register_name = register.upper()
        if register_name not in REGISTERS:
            raise Exception("'{reg}' is not a valid {platform} register.".format(
                reg=register_name, platform='x64' if is_64bit() else 'x86'
            ))

        return getattr(
            pluginsdk._scriptapi.register,
            '{method}{register}'.format(
                method='Get' if get else 'Set',
                register=register_name
            )
        )

    @staticmethod
    def _get_func(self, register):
        return self.__get_reg_function(register)()

    @staticmethod    
    def _set_func(self, value, register):
        self.__get_reg_function(register, get=False)(value)
        if self.refresh_gui:
            GuiUpdateAllViews()

