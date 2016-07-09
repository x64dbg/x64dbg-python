import ctypes
from .. import x64dbg


MAX_COMMENT_SIZE = 512


def Set(addr, text, manual = False):
    return x64dbg.Comment_Set(addr, text, manual)

def SetInfo(info):
    return x64dbg.Comment_Set(info)

def Get(addr):
    text = ctypes.create_string_buffer(MAX_COMMENT_SIZE)
    res =  x64dbg.Comment_Get(addr, text)
    if res:
        return text.value

def GetInfo(addr):
    info = x64dbg.CommentInfo()
    res = x64dbg.Comment_GetInfo(addr, info)
    if res:
        return info

def Delete(addr):
    return x64dbg.Comment_Delete(addr)

def DeleteRange(start, end):
    return x64dbg.Comment_DeleteRange(start, end)

def Clear():
    x64dbg.Comment_Clear()

def GetList():
    l = x64dbg.ListInfo()
    res = x64dbg.Comment_GetList(l)
    if res:
        return x64dbg.GetCommentInfoList(l)
