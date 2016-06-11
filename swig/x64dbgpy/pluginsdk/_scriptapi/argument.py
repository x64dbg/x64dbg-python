import ctypes
from .. import x64dbg


def Add(start, end, manual, instructionCount = 0):
    return x64dbg.Argument_Add(start, end, manual, instructionCount)

def AddInfo(info):
    return x64dbg.Argument_Add(info)

def Get(addr):
    res, start, end, instructionCount = x64dbg.Argument_Get(addr, 0, 0, 0)
    return start, end, instructionCount if res else None

def GetInfo(addr):
    info = x64dbg.ArgumentInfo()
    res = x64dbg.Argument_GetInfo(addr, info)
    if res:
        return info

def Overlaps(start, end):
    return x64dbg.Argument_Overlaps(start, end)

def Delete(addr):
    return x64dbg.Argument_Delete(addr)

def DeleteRange(start, end, deleteManual = False):
    return x64dbg.Argument_DeleteRange(start, end, deleteManual)

def Clear():
    x64dbg.Argument_Clear()

def GetList():
    l = x64dbg.ListInfo()
    res = x64dbg.Argument_GetList(l)
    if res:
        return x64dbg.GetArgumentInfoList(l)
