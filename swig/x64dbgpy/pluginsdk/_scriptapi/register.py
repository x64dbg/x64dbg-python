from x64dbgpy.utils import is_64bit
from .. import x64dbg


def Size():
    return x64dbg.Size()


# x86 Registers
def GetEAX():
    return x64dbg.GetEAX()

def SetEAX(value):
    return x64dbg.SetEAX(value)

def GetAX():
    return x64dbg.GetAX()

def SetAX(value):
    return x64dbg.SetAX(value)

def GetAH():
    return x64dbg.GetAH()

def SetAH(value):
    return x64dbg.SetAH(value)

def GetAL():
    return x64dbg.GetAL()

def SetAL(value):
    return x64dbg.SetAL(value)

def GetEBX():
    return x64dbg.GetEBX()

def SetEBX(value):
    return x64dbg.SetEBX(value)

def GetBX():
    return x64dbg.GetBX()

def SetBX(value):
    return x64dbg.SetBX(value)

def GetBH():
    return x64dbg.GetBH()

def SetBH(value):
    return x64dbg.SetBH(value)

def GetBL():
    return x64dbg.GetBL()

def SetBL(value):
    return x64dbg.SetBL(value)

def GetECX():
    return x64dbg.GetECX()

def SetECX(value):
    return x64dbg.SetECX(value)

def GetCX():
    return x64dbg.GetCX()

def SetCX(value):
    return x64dbg.SetCX(value)

def GetCH():
    return x64dbg.GetCH()

def SetCH(value):
    return x64dbg.SetCH(value)

def GetCL():
    return x64dbg.GetCL()

def SetCL(value):
    return x64dbg.SetCL(value)

def GetEDX():
    return x64dbg.GetEDX()

def SetEDX(value):
    return x64dbg.SetEDX(value)

def GetDX():
    return x64dbg.GetDX()

def SetDX(value):
    return x64dbg.SetDX(value)

def GetDH():
    return x64dbg.GetDH()

def SetDH(value):
    return x64dbg.SetDH(value)

def GetDL():
    return x64dbg.GetDL()

def SetDL(value):
    return x64dbg.SetDL(value)

def GetEDI():
    return x64dbg.GetEDI()

def SetEDI(value):
    return x64dbg.SetEDI(value)

def GetDI():
    return x64dbg.GetDI()

def SetDI(value):
    return x64dbg.SetDI(value)

def GetESI():
    return x64dbg.GetESI()

def SetESI(value):
    return x64dbg.SetESI(value)

def GetSI():
    return x64dbg.GetSI()

def SetSI(value):
    return x64dbg.SetSI(value)

def GetEBP():
    return x64dbg.GetEBP()

def SetEBP(value):
    return x64dbg.SetEBP(value)

def GetBP():
    return x64dbg.GetBP()

def SetBP(value):
    return x64dbg.SetBP(value)

def GetESP():
    return x64dbg.GetESP()

def SetESP(value):
    return x64dbg.SetESP(value)

def GetSP():
    return x64dbg.GetSP()

def SetSP(value):
    return x64dbg.SetSP(value)

def GetEIP():
    return x64dbg.GetEIP()

def SetEIP(value):
    return x64dbg.SetEIP(value)


# x86 Debug Registers
def GetDR0():
    return x64dbg.GetDR0()

def SetDR0(value):
    return x64dbg.SetDR0(value)

def GetDR1():
    return x64dbg.GetDR1()

def SetDR1(value):
    return x64dbg.SetDR1(value)

def GetDR2():
    return x64dbg.GetDR2()

def SetDR2(value):
    return x64dbg.SetDR2(value)

def GetDR3():
    return x64dbg.GetDR3()

def SetDR3(value):
    return x64dbg.SetDR3(value)

def GetDR6():
    return x64dbg.GetDR6()

def SetDR6(value):
    return x64dbg.SetDR6(value)

def GetDR7():
    return x64dbg.GetDR7()

def SetDR7(value):
    return x64dbg.SetDR7(value)


# x64 Registers
if is_64bit():
    def GetRAX():
        return x64dbg.GetRAX()

    def SetRAX(value):
        return x64dbg.SetRAX(value)

    def GetRBX():
        return x64dbg.GetRBX()

    def SetRBX(value):
        return x64dbg.SetRBX(value)

    def GetRCX():
        return x64dbg.GetRCX()

    def SetRCX(value):
        return x64dbg.SetRCX(value)

    def GetRDX():
        return x64dbg.GetRDX()

    def SetRDX(value):
        return x64dbg.SetRDX(value)

    def GetRSI():
        return x64dbg.GetRSI()

    def SetRSI(value):
        return x64dbg.SetRSI(value)

    def GetSIL():
        return x64dbg.GetSIL()

    def SetSIL(value):
        return x64dbg.SetSIL(value)

    def GetRDI():
        return x64dbg.GetRDI()

    def SetRDI(value):
        return x64dbg.SetRDI(value)

    def GetDIL():
        return x64dbg.GetDIL()

    def SetDIL(value):
        return x64dbg.SetDIL(value)

    def GetRBP():
        return x64dbg.GetRBP()

    def SetRBP(value):
        return x64dbg.SetRBP(value)

    def GetBPL():
        return x64dbg.GetBPL()

    def SetBPL(value):
        return x64dbg.SetBPL(value)

    def GetRSP():
        return x64dbg.GetRSP()

    def SetRSP(value):
        return x64dbg.SetRSP(value)

    def GetSPL():
        return x64dbg.GetSPL()

    def SetSPL(value):
        return x64dbg.SetSPL(value)

    def GetRIP():
        return x64dbg.GetRIP()

    def SetRIP(value):
        return x64dbg.SetRIP(value)

    def GetR8():
        return x64dbg.GetR8()

    def SetR8(value):
        return x64dbg.SetR8(value)

    def GetR8D():
        return x64dbg.GetR8D()

    def SetR8D(value):
        return x64dbg.SetR8D(value)

    def GetR8W():
        return x64dbg.GetR8W()

    def SetR8W(value):
        return x64dbg.SetR8W(value)

    def GetR8B():
        return x64dbg.GetR8B()

    def SetR8B(value):
        return x64dbg.SetR8B(value)

    def GetR9():
        return x64dbg.GetR9()

    def SetR9(value):
        return x64dbg.SetR9(value)

    def GetR9D():
        return x64dbg.GetR9D()

    def SetR9D(value):
        return x64dbg.SetR9D(value)

    def GetR9W():
        return x64dbg.GetR9W()

    def SetR9W(value):
        return x64dbg.SetR9W(value)

    def GetR9B():
        return x64dbg.GetR9B()

    def SetR9B(value):
        return x64dbg.SetR9B(value)

    def GetR10():
        return x64dbg.GetR10()

    def SetR10(value):
        return x64dbg.SetR10(value)

    def GetR10D():
        return x64dbg.GetR10D()

    def SetR10D(value):
        return x64dbg.SetR10D(value)

    def GetR10W():
        return x64dbg.GetR10W()

    def SetR10W(value):
        return x64dbg.SetR10W(value)

    def GetR10B():
        return x64dbg.GetR10B()

    def SetR10B(value):
        return x64dbg.SetR10B(value)

    def GetR11():
        return x64dbg.GetR11()

    def SetR11(value):
        return x64dbg.SetR11(value)

    def GetR11D():
        return x64dbg.GetR11D()

    def SetR11D(value):
        return x64dbg.SetR11D(value)

    def GetR11W():
        return x64dbg.GetR11W()

    def SetR11W(value):
        return x64dbg.SetR11W(value)

    def GetR11B():
        return x64dbg.GetR11B()

    def SetR11B(value):
        return x64dbg.SetR11B(value)

    def GetR12():
        return x64dbg.GetR12()

    def SetR12(value):
        return x64dbg.SetR12(value)

    def GetR12D():
        return x64dbg.GetR12D()

    def SetR12D(value):
        return x64dbg.SetR12D(value)

    def GetR12W():
        return x64dbg.GetR12W()

    def SetR12W(value):
        return x64dbg.SetR12W(value)

    def GetR12B():
        return x64dbg.GetR12B()

    def SetR12B(value):
        return x64dbg.SetR12B(value)

    def GetR13():
        return x64dbg.GetR13()

    def SetR13(value):
        return x64dbg.SetR13(value)

    def GetR13D():
        return x64dbg.GetR13D()

    def SetR13D(value):
        return x64dbg.SetR13D(value)

    def GetR13W():
        return x64dbg.GetR13W()

    def SetR13W(value):
        return x64dbg.SetR13W(value)

    def GetR13B():
        return x64dbg.GetR13B()

    def SetR13B(value):
        return x64dbg.SetR13B(value)

    def GetR14():
        return x64dbg.GetR14()

    def SetR14(value):
        return x64dbg.SetR14(value)

    def GetR14D():
        return x64dbg.GetR14D()

    def SetR14D(value):
        return x64dbg.SetR14D(value)

    def GetR14W():
        return x64dbg.GetR14W()

    def SetR14W(value):
        return x64dbg.SetR14W(value)

    def GetR14B():
        return x64dbg.GetR14B()

    def SetR14B(value):
        return x64dbg.SetR14B(value)

    def GetR15():
        return x64dbg.GetR15()

    def SetR15(value):
        return x64dbg.SetR15(value)

    def GetR15D():
        return x64dbg.GetR15D()

    def SetR15D(value):
        return x64dbg.SetR15D(value)

    def GetR15W():
        return x64dbg.GetR15W()

    def SetR15W(value):
        return x64dbg.SetR15W(value)

    def GetR15B():
        return x64dbg.GetR15B()

    def SetR15B(value):
        return x64dbg.SetR15B(value)


# Generic Registers
def GetCIP():
    return x64dbg.GetCIP()

def SetCIP(value):
    return x64dbg.SetCIP(value)

def GetCSP():
    return x64dbg.GetCSP()

def SetCSP(value):
    return x64dbg.SetCSP(value)
