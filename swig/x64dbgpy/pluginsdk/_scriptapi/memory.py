from x64dbgpy.utils import is_64bit
from .. import x64dbg


def Read(addr, size):
    read_bytes = bytearray(size)
    result, read_size = x64dbg.Memory_Read(addr, read_bytes, size)
    return bytes(read_bytes[:read_size])

def Write(addr, data):
    result, write_size = x64dbg.Memory_Write(addr, data, len(data))
    return result

def IsValidPtr(addr):
    return x64dbg.IsValidPtr(addr)

def RemoteAlloc(size, addr=0):
    return x64dbg.RemoteAlloc(addr, size)

def RemoteFree(addr):
    return x64dbg.RemoteFree(addr)

def GetProtect(addr, reserved=False, cache=True):
    return x64dbg.GetProtect(addr, reserved, cache)

def GetBase(addr, reserved=False, cache=True):
    return x64dbg.GetBase(addr, reserved, cache)

def GetSize(addr, reserved=False, cache=True):
    return x64dbg.GetSize(addr, reserved, cache)

def ReadByte(addr):
    return x64dbg.ReadByte(addr)

def WriteByte(addr, data):
    return x64dbg.WriteByte(addr, data)

def ReadWord(addr):
    return x64dbg.ReadWord(addr)

def WriteWord(addr, data):
    return x64dbg.WriteWord(addr, data)

def ReadDword(addr):
    return x64dbg.ReadDword(addr)

def WriteDword(addr, data):
    return x64dbg.WriteDword(addr, data)

if is_64bit():
    def ReadQword(addr):
        return x64dbg.ReadQword(addr)

    def WriteQword(addr, data):
        return x64dbg.WriteQword(addr, data)

def ReadPtr(addr):
    return x64dbg.ReadPtr(addr)

def WritePtr(addr, data):
    return x64dbg.WritePtr(addr, data)
