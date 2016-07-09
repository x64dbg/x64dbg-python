from .. import x64dbg


GUI_MAX_LINE_SIZE = 65536


# Script::Gui
def Gui_SelectionGet(window):
    result, start, end = x64dbg.Gui_SelectionGet(window)
    if result:
        return start, end

def Gui_SelectionSet(window, start, end):
    return x64dbg.Gui_SelectionSet(window, start, end)

def Gui_SelectionGetStart(window):
    return x64dbg.Gui_SelectionGetStart(window)

def Gui_SelectionGetEnd(window):
    return x64dbg.Gui_SelectionGetEnd(window)

def Message(message):
    x64dbg.Message(message)

def MessageYesNo(message):
    return x64dbg.MessageYesNo(message)

def InputLine(title):
    text = ctypes.create_string_buffer(GUI_MAX_LINE_SIZE)
    res =  x64dbg.InputLine(title, text)
    if res:
        return text.value

def InputValue(title):
    res, value =  x64dbg.InputValue(title)
    if res:
        return value

def Refresh():
    x64dbg.Refresh()


# Script::Gui::Disassembly
def Disassembly_SelectionGet():
    result, start, end = x64dbg.Disassembly_SelectionGet()
    if result:
        return start, end

def Disassembly_SelectionSet(start, end):
    return x64dbg.Disassembly_SelectionSet(start, end)

def Disassembly_SelectionGetStart():
    return x64dbg.Disassembly_SelectionGetStart()

def Disassembly_SelectionGetEnd():
    return x64dbg.Disassembly_SelectionGetEnd()


# Script::Gui::Dump
def Dump_SelectionGet():
    result, start, end = x64dbg.Dump_SelectionGet()
    if result:
        return start, end

def Dump_SelectionSet(start, end):
    return x64dbg.Dump_SelectionSet(start, end)

def Dump_SelectionGetStart():
    return x64dbg.Dump_SelectionGetStart()

def Dump_SelectionGetEnd():
    return x64dbg.Dump_SelectionGetEnd()


# Script::Gui::Stack
def Stack_SelectionGet():
    result, start, end = x64dbg.Stack_SelectionGet()
    if result:
        return start, end

def Stack_SelectionSet(start, end):
    return x64dbg.Stack_SelectionSet(start, end)

def Stack_SelectionGetStart():
    return x64dbg.Stack_SelectionGetStart()

def Stack_SelectionGetEnd():
    return x64dbg.Stack_SelectionGetEnd()
