from .. import _x64dbg


def Wait():
    """
    making the debugger wait.
    """
    _x64dbg.Wait()

def Run():
    """
    making the debuggerr run.
    """
    _x64dbg.Run()

def Stop():
    """
    making the debugger stop.
    """
    _x64dbg.Stop()

def StepIn():
    """
    Step into a instruction.
    """
    _x64dbg.StepIn()

def StepOver():
    """
    Step over a instruction.
    """
    _x64dbg.StepOver()

def StepOut():
    """
    Step Out of instructions.
    """
    _x64dbg.StepOut()
