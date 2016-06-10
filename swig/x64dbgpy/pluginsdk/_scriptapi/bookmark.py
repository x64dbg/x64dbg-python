import ctypes
from .. import x64dbg


def Set(addr, manual = False):
    return x64dbg.Bookmark_Set(addr, manual)

def SetInfo(info):
    return x64dbg.Bookmark_Set(info)

def Get(addr):
    return x64dbg.Bookmark_Get(addr)

def GetInfo(addr):
    info = x64dbg.BookmarkInfo()
    res = x64dbg.Bookmark_GetInfo(addr, info)
    if res:
        return info

def Delete(addr):
    return x64dbg.Bookmark_Delete(addr)

def DeleteRange(start, end):
    return x64dbg.Bookmark_DeleteRange(start, end)

def Clear():
    x64dbg.Bookmark_Clear()

def GetList():
    l = x64dbg.ListInfo()
    res = x64dbg.Bookmark_GetList(l)
    if res:
        return x64dbg.GetBookmarkInfoList(l)
