from .. import x64dbg


def Find(data, pattern):
    return x64dbg.Find(data, len(data), pattern)

def FindMem(start, size, pattern):
    return x64dbg.FindMem(start, size, pattern)

def Write(data, pattern):
    x64dbg.Write(data, len(data), pattern)

def WriteMem(start, size, pattern):
    x64dbg.WriteMem(start, size, pattern)

def SearchAndReplace(data, searchpattern, replacepattern):
    return x64dbg.SearchAndReplace(data, len(data), searchpattern, replacepattern)

def SearchAndReplaceMem(start, size, searchpattern, replacepattern):
    return x64dbg.SearchAndReplaceMem(start, size, searchpattern, replacepattern)
