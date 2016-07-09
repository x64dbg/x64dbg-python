import ctypes
from .. import x64dbg


class SymbolType:
    Function = x64dbg.Function
    Import = x64dbg.Import
    Export = x64dbg.Export


def GetList():
    l = x64dbg.ListInfo()
    res = x64dbg.Symbol_GetList(l)
    if res:
        return x64dbg.GetSymbolInfoList(l)
