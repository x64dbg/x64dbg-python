import ctypes
from .. import x64dbg


MAX_MODULE_SIZE = 256
MAX_PATH = 260


def InfoFromAddr(addr):
    info = x64dbg.ModuleInfo()
    res = x64dbg.InfoFromAddr(addr, info)
    if res:
        return info

def InfoFromName(name):
    info = x64dbg.ModuleInfo()
    result = x64dbg.InfoFromName(name, info)
    if result:
        return info

def BaseFromAddr(addr):
    return x64dbg.BaseFromAddr(addr)

def BaseFromName(name):
    return x64dbg.BaseFromName(name)

def SizeFromAddr(addr):
    return x64dbg.SizeFromAddr(addr)

def SizeFromName(name):
    return x64dbg.SizeFromName(name)

def NameFromAddr(addr):
    name = ctypes.create_string_buffer(MAX_MODULE_SIZE)
    result = x64dbg.NameFromAddr(addr, name)
    if result:
        return name.value

def PathFromAddr(addr):
    path = ctypes.create_string_buffer(MAX_PATH)
    result = x64dbg.PathFromAddr(addr, path)
    if result:
        return path.value

def PathFromName(name):
    path = ctypes.create_string_buffer(MAX_PATH)
    result = x64dbg.PathFromName(name, path)
    if result:
        return path.value

def EntryFromAddr(addr):
    return x64dbg.EntryFromAddr(addr)

def EntryFromName(name):
    return x64dbg.EntryFromName(name)

def SectionCountFromAddr(addr):
    return x64dbg.SectionCountFromAddr(addr)

def SectionCountFromName(name):
    return x64dbg.SectionCountFromName(name)

def SectionFromAddr(addr, number):
    section = x64dbg.ModuleSectionInfo()
    result = x64dbg.SectionFromAddr(addr, number, section)
    if result:
        return section

def SectionFromName(name, number):
    section = x64dbg.ModuleSectionInfo()
    result = x64dbg.SectionFromName(name, number, section)
    if result:
        return section

def SectionListFromAddr(addr):
    l = x64dbg.ListInfo()
    res = x64dbg.SectionListFromAddr(addr, l)
    if res:
        return x64dbg.GetModuleSectionInfoList(l)

def SectionListFromName(name):
    l = x64dbg.ListInfo()
    res = x64dbg.SectionListFromName(addr, l)
    if res:
        return x64dbg.GetModuleSectionInfoList(l)

def GetMainModuleInfo():
    info = x64dbg.ModuleInfo()
    result = x64dbg.GetMainModuleInfo(info)
    if result:
        return info

def GetMainModuleBase():
    return x64dbg.GetMainModuleBase()

def GetMainModuleSize():
    return x64dbg.GetMainModuleSize()

def GetMainModuleEntry():
    return x64dbg.GetMainModuleEntry()

def GetMainModuleSectionCount():
    return x64dbg.GetMainModuleSectionCount()

def GetMainModuleName():
    name = ctypes.create_string_buffer(MAX_MODULE_SIZE)
    result = x64dbg.GetMainModuleName(name)
    if result:
        return name.value

def GetMainModulePath():
    path = ctypes.create_string_buffer(MAX_PATH)
    result = x64dbg.GetMainModulePath(path)
    if result:
        return path.value

def GetMainModuleSectionList():
    l = x64dbg.ListInfo()
    res = x64dbg.GetMainModuleSectionList(l)
    if res:
        return x64dbg.GetModuleSectionInfoList(l)

def GetList():
    l = x64dbg.ListInfo()
    res = x64dbg.GetList(l)
    if res:
        return x64dbg.GetModuleInfoList(l)