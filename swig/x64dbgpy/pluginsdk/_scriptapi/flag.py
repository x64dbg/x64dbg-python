from .. import x64dbg


class FlagEnum:
    ZF = x64dbg.ZF
    OF = x64dbg.OF
    CF = x64dbg.CF
    PF = x64dbg.PF
    SF = x64dbg.SF
    TF = x64dbg.TF
    AF = x64dbg.AF
    DF = x64dbg.DF
    IF = x64dbg.IF


def Flag_Get(flag):
    return x64dbg.Flag_Get(flag)

def Flag_Set(flag, value):
    return x64dbg.Flag_Set(flag, value)


def GetZF():
    return x64dbg.GetZF()

def SetZF(value):
    return x64dbg.SetZF(value)

def GetOF():
    return x64dbg.GetOF()

def SetOF(value):
    return x64dbg.SetOF(value)

def GetCF():
    return x64dbg.GetCF()

def SetCF(value):
    return x64dbg.SetCF(value)

def GetPF():
    return x64dbg.GetPF()

def SetPF(value):
    return x64dbg.SetPF(value)

def GetSF():
    return x64dbg.GetSF()

def SetSF(value):
    return x64dbg.SetSF(value)

def GetTF():
    return x64dbg.GetTF()

def SetTF(value):
    return x64dbg.SetTF(value)

def GetAF():
    return x64dbg.GetAF()

def SetAF(value):
    return x64dbg.SetAF(value)

def GetDF():
    return x64dbg.GetDF()

def SetDF(value):
    return x64dbg.SetDF(value)

def GetIF():
    return x64dbg.GetIF()

def SetIF(value):
    return x64dbg.SetIF(value)
