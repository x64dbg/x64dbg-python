from .. import x64dbg


def Find(data, pattern):
    return x64dbg.Find(data, pattern)

def FindMem(start, size, pattern):
    return x64dbg.FindMem(start, size, pattern)

def PatternWrite(data, pattern):
    x64dbg.Pattern_Write(data, pattern)

def PatternWriteMem(start, size, pattern):
    x64dbg.Pattern_WriteMem(start, size, pattern)

def SearchAndReplace(data, searchpattern, replacepattern):
    return x64dbg.SearchAndReplace(data, searchpattern, replacepattern)

def SearchAndReplaceMem(start, size, searchpattern, replacepattern):
    return x64dbg.SearchAndReplaceMem(start, size, searchpattern, replacepattern)
