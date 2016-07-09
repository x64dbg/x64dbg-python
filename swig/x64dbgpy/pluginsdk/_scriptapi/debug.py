from .. import x64dbg


class HardwareType:
    HardwareAccess = x64dbg.HardwareAccess
    HardwareWrite = x64dbg.HardwareWrite
    HardwareExecute = x64dbg.HardwareExecute


def Wait():
    x64dbg.Wait()

def Run():
    x64dbg.Run()

def Stop():
    x64dbg.Stop()

def StepIn():
    x64dbg.StepIn()

def StepOver():
    x64dbg.StepOver()

def StepOut():
    x64dbg.StepOut()

def SetBreakpoint(address):
    return x64dbg.SetBreakpoint(address)

def DeleteBreakpoint(address):
    return x64dbg.DeleteBreakpoint(address)

def SetHardwareBreakpoint(address, type = HardwareType.HardwareExecute):
    return x64dbg.SetHardwareBreakpoint(address, type)

def DeleteHardwareBreakpoint(address):
    return x64dbg.DeleteHardwareBreakpoint(address)

