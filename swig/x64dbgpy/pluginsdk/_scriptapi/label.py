import ctypes
from .. import x64dbg


MAX_LABEL_SIZE = 256


def Set(addr, text, manual = False):
    return x64dbg.Label_Set(addr, text, manual)

def SetInfo(info):
    return x64dbg.Label_Set(info)

def FromString(label):
    res, addr = x64dbg.FromString(label)
    if res:
        return addr

def Get(addr):
    text = ctypes.create_string_buffer(MAX_LABEL_SIZE)
    res =  x64dbg.Label_Get(addr, text)
    if res:
        return text.value

def GetInfo(addr):
    info = x64dbg.LabelInfo()
    res = x64dbg.Label_GetInfo(addr, info)
    if res:
        return info

def Delete(addr):
    return x64dbg.Label_Delete(addr)

def DeleteRange(start, end):
    return x64dbg.Label_DeleteRange(start, end)

def Clear():
    x64dbg.Label_Clear()

def GetList():
    l = x64dbg.ListInfo()
    res = x64dbg.Label_GetList(l)
    if res:
        return x64dbg.GetLabelInfoList(l)
