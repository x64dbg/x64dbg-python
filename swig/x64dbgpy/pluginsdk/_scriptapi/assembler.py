import ctypes
from .. import x64dbg


MAX_ERROR_SIZE = 512
MAX_STRING = 512


def Assemble(addr, instruction):
    dest = ctypes.create_string_buffer(MAX_STRING)
    result, size = x64dbg.Assemble(addr, dest, instruction)
    if result:
        return dest[:size].encode('hex')

def AssembleEx(addr, instruction):
    error = ctypes.create_string_buffer(MAX_ERROR_SIZE)
    dest = ctypes.create_string_buffer(MAX_STRING)
    result, size = x64dbg.AssembleEx(addr, dest, instruction, error)
    if not result:
        raise Exception(error.value)
    return dest[:size].encode('hex')

def AssembleMem(addr, instruction):
    return x64dbg.AssembleMem(addr, instruction)

def AssembleMemEx(addr, instruction, fillnop):
    error = ctypes.create_string_buffer(MAX_ERROR_SIZE)
    result, size = x64dbg.AssembleMemEx(addr, instruction, error, fillnop)
    if not result:
        raise Exception(error.value)
    return result
