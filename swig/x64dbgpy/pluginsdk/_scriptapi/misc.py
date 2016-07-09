from .. import x64dbg


def ParseExpression(expression):
    res, value = x64dbg.ParseExpression(expression)
    if res:
        return value

def RemoteGetProcAddress(module, api):
    return x64dbg.RemoteGetProcAddress(module, api)

def ResolveLabel(label):
    return x64dbg.ResolveLabel(label)

def Alloc(size):
    return x64dbg.Alloc(size)

def Free(ptr):
    return x64dbg.Free(ptr)
