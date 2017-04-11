#include <windows.h>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include "../pluginsdk/_plugins.h"

#include "../pluginsdk/_scriptapi_argument.h"
#include "../pluginsdk/_scriptapi_assembler.h"
#include "../pluginsdk/_scriptapi_bookmark.h"
#include "../pluginsdk/_scriptapi_comment.h"
#include "../pluginsdk/_scriptapi_debug.h"
#include "../pluginsdk/_scriptapi_flag.h"
#include "../pluginsdk/_scriptapi_function.h"
#include "../pluginsdk/_scriptapi_gui.h"
#include "../pluginsdk/_scriptapi_label.h"
#include "../pluginsdk/_scriptapi_memory.h"
#include "../pluginsdk/_scriptapi_misc.h"
#include "../pluginsdk/_scriptapi_module.h"
#include "../pluginsdk/_scriptapi_pattern.h"
#include "../pluginsdk/_scriptapi_register.h"
#include "../pluginsdk/_scriptapi_stack.h"
#include "../pluginsdk/_scriptapi_symbol.h"

#include "../pluginsdk/capstone/capstone.h"
#include "../pluginsdk/DeviceNameResolver/DeviceNameResolver.h"
#include "../pluginsdk/jansson/jansson.h"
#include "../pluginsdk/lz4/lz4file.h"
#include "../pluginsdk/TitanEngine/TitanEngine.h"
#include "../pluginsdk/XEDParse/XEDParse.h"
#include "../pluginsdk/yara/yara.h"

#ifdef _WIN64
#pragma comment(lib, "../pluginsdk/x64dbg.lib")
#pragma comment(lib, "../pluginsdk/x64bridge.lib")
#pragma comment(lib, "../pluginsdk/capstone/capstone_x64.lib")
#pragma comment(lib, "../pluginsdk/DeviceNameResolver/DeviceNameResolver_x64.lib")
#pragma comment(lib, "../pluginsdk/jansson/jansson_x64.lib")
#pragma comment(lib, "../pluginsdk/lz4/lz4_x64.lib")
#pragma comment(lib, "../pluginsdk/TitanEngine/TitanEngine_x64.lib")
#pragma comment(lib, "../pluginsdk/XEDParse/XEDParse_x64.lib")
#pragma comment(lib, "../pluginsdk/yara/yara_x64.lib")
#else
#pragma comment(lib, "../pluginsdk/x32dbg.lib")
#pragma comment(lib, "../pluginsdk/x32bridge.lib")
#pragma comment(lib, "../pluginsdk/capstone/capstone_x86.lib")
#pragma comment(lib, "../pluginsdk/DeviceNameResolver/DeviceNameResolver_x86.lib")
#pragma comment(lib, "../pluginsdk/jansson/jansson_x86.lib")
#pragma comment(lib, "../pluginsdk/lz4/lz4_x86.lib")
#pragma comment(lib, "../pluginsdk/TitanEngine/TitanEngine_x86.lib")
#pragma comment(lib, "../pluginsdk/XEDParse/XEDParse_x86.lib")
#pragma comment(lib, "../pluginsdk/yara/yara_x86.lib")
#endif //_WIN64

using namespace Script;
namespace py = pybind11;

struct PyMemory
{
    PyMemory() = delete;
    PyMemory(const PyMemory &) = delete;
    PyMemory(PyMemory &&) = delete;

    static py::bytes Read(duint addr, duint size)
    {
        auto data = std::unique_ptr<char[]>(new char[size]);
        duint sizeRead = 0;
        Memory::Read(addr, data.get(), size, &sizeRead);
        return py::bytes(data.get(), sizeRead);
    }

    static bool Write(duint addr, py::bytes data)
    {
        char* ptr;
        ssize_t size;
        PYBIND11_BYTES_AS_STRING_AND_SIZE(data.ptr(), &ptr, &size);
        return Memory::Write(addr, ptr, size, nullptr);
    }

    static duint RemoteAlloc(duint size)
    {
        return Memory::RemoteAlloc(0, size);
    }

    static unsigned int GetProtect(duint addr)
    {
        return Memory::GetProtect(addr);
    }

    static duint GetBase(duint addr)
    {
        return Memory::GetBase(addr);
    }

    static duint GetSize(duint addr)
    {
        return Memory::GetSize(addr);
    }
};

struct PyRegister
{
};

PYBIND11_PLUGIN(scriptapi)
{
#define arg(x) py::arg(#x)

    py::module m("scriptapi", "Python module to wrap the x64dbg script api.");

    py::class_<PyMemory>(m, "Memory")
    .def_static("read", PyMemory::Read, arg(addr), arg(size), "Read `size` bytes at `addr`.")
    .def_static("write", PyMemory::Write, arg(addr), arg(data), "Write `data` to `addr`.")
    .def_static("valid", Memory::IsValidPtr, arg(addr), "Returns if `addr` is a valid pointer.")
    .def_static("alloc", PyMemory::RemoteAlloc, arg(size), "Allocates `size` memory in the process.")
    .def_static("free", Memory::RemoteFree, arg(addr), "Frees memory at `addr` in the process.")
    .def_static("protection", PyMemory::GetProtect, arg(addr), "Get the page protection constant from `addr`.")
    .def_static("base", PyMemory::GetBase, arg(addr), "Get the base address of the page at `addr`.")
    .def_static("size", PyMemory::GetSize, arg(addr), "Get the size of the page at `addr`.")
    .def_static("read_byte", Memory::ReadByte, arg(addr), "Read a byte at `addr`.")
    .def_static("write_byte", Memory::WriteByte, arg(addr), arg(value), "Write `value` as a byte to `addr`.")
    .def_static("read_word", Memory::ReadWord, arg(addr), "Read a word at `addr`.")
    .def_static("write_word", Memory::WriteWord, arg(addr), arg(value), "Write `value` as a word to `addr`.")
    .def_static("read_dword", Memory::ReadDword, arg(addr), "Read a dword at `addr`.")
    .def_static("write_dword", Memory::WriteDword, arg(addr), arg(value), "Write `value` as a dword to `addr`.")
    .def_static("read_qword", Memory::ReadQword, arg(addr), "Read a qword at `addr`.")
    .def_static("write_qword", Memory::WriteQword, arg(addr), arg(value), "Write `value` as a qword to `addr`.")
    .def_static("read_ptr", Memory::ReadPtr, arg(addr), "Read a pointer at `addr`.")
    .def_static("write_ptr", Memory::WritePtr, arg(addr), arg(value), "Write `value` as a pointer to `addr`.");

    py::class_<PyRegister>(m, "Registers")
    .def_property_static("dr0", Register::GetDR0, Register::SetDR0)
    .def_property_static("dr1", Register::GetDR1, Register::SetDR1)
    .def_property_static("dr2", Register::GetDR2, Register::SetDR2)
    .def_property_static("dr3", Register::GetDR3, Register::SetDR3)
    .def_property_static("dr6", Register::GetDR6, Register::SetDR6)
    .def_property_static("dr7", Register::GetDR7, Register::SetDR7)

    .def_property_static("eax", Register::GetEAX, Register::SetEAX)
    .def_property_static("ax", Register::GetAX, Register::SetAX)
    .def_property_static("ah", Register::GetAH, Register::SetAH)
    .def_property_static("al", Register::GetAL, Register::SetAL)
    .def_property_static("ebx", Register::GetEBX, Register::SetEBX)
    .def_property_static("bx", Register::GetBX, Register::SetBX)
    .def_property_static("bh", Register::GetBH, Register::SetBH)
    .def_property_static("bl", Register::GetBL, Register::SetBL)
    .def_property_static("ecx", Register::GetECX, Register::SetECX)
    .def_property_static("cx", Register::GetCX, Register::SetCX)
    .def_property_static("ch", Register::GetCH, Register::SetCH)
    .def_property_static("cl", Register::GetCL, Register::SetCL)
    .def_property_static("edx", Register::GetEDX, Register::SetEDX)
    .def_property_static("dx", Register::GetDX, Register::SetDX)
    .def_property_static("dh", Register::GetDH, Register::SetDH)
    .def_property_static("dl", Register::GetDL, Register::SetDL)
    .def_property_static("edi", Register::GetEDI, Register::SetEDI)
    .def_property_static("di", Register::GetDI, Register::SetDI)
    .def_property_static("esi", Register::GetESI, Register::SetESI)
    .def_property_static("si", Register::GetSI, Register::SetSI)
    .def_property_static("ebp", Register::GetEBP, Register::SetEBP)
    .def_property_static("bp", Register::GetBP, Register::SetBP)
    .def_property_static("esp", Register::GetESP, Register::SetESP)
    .def_property_static("sp", Register::GetSP, Register::SetSP)
    .def_property_static("eip", Register::GetEIP, Register::SetEIP)

#ifdef _WIN64
    .def_property_static("rax", Register::GetRAX, Register::SetRAX)
    .def_property_static("rbx", Register::GetRBX, Register::SetRBX)
    .def_property_static("rcx", Register::GetRCX, Register::SetRCX)
    .def_property_static("rdx", Register::GetRDX, Register::SetRDX)
    .def_property_static("rsi", Register::GetRSI, Register::SetRSI)
    .def_property_static("sil", Register::GetSIL, Register::SetSIL)
    .def_property_static("rdi", Register::GetRDI, Register::SetRDI)
    .def_property_static("dil", Register::GetDIL, Register::SetDIL)
    .def_property_static("rbp", Register::GetRBP, Register::SetRBP)
    .def_property_static("bpl", Register::GetBPL, Register::SetBPL)
    .def_property_static("rsp", Register::GetRSP, Register::SetRSP)
    .def_property_static("spl", Register::GetSPL, Register::SetSPL)
    .def_property_static("rip", Register::GetRIP, Register::SetRIP)
    .def_property_static("r8", Register::GetR8, Register::SetR8)
    .def_property_static("r8d", Register::GetR8D, Register::SetR8D)
    .def_property_static("r8w", Register::GetR8W, Register::SetR8W)
    .def_property_static("r8b", Register::GetR8B, Register::SetR8B)
    .def_property_static("r9", Register::GetR9, Register::SetR9)
    .def_property_static("r9d", Register::GetR9D, Register::SetR9D)
    .def_property_static("r9w", Register::GetR9W, Register::SetR9W)
    .def_property_static("r9b", Register::GetR9B, Register::SetR9B)
    .def_property_static("r10", Register::GetR10, Register::SetR10)
    .def_property_static("r10d", Register::GetR10D, Register::SetR10D)
    .def_property_static("r10w", Register::GetR10W, Register::SetR10W)
    .def_property_static("r10b", Register::GetR10B, Register::SetR10B)
    .def_property_static("r11", Register::GetR11, Register::SetR11)
    .def_property_static("r11d", Register::GetR11D, Register::SetR11D)
    .def_property_static("r11w", Register::GetR11W, Register::SetR11W)
    .def_property_static("r11b", Register::GetR11B, Register::SetR11B)
    .def_property_static("r12", Register::GetR12, Register::SetR12)
    .def_property_static("r12d", Register::GetR12D, Register::SetR12D)
    .def_property_static("r12w", Register::GetR12W, Register::SetR12W)
    .def_property_static("r12b", Register::GetR12B, Register::SetR12B)
    .def_property_static("r13", Register::GetR13, Register::SetR13)
    .def_property_static("r13d", Register::GetR13D, Register::SetR13D)
    .def_property_static("r13w", Register::GetR13W, Register::SetR13W)
    .def_property_static("r13b", Register::GetR13B, Register::SetR13B)
    .def_property_static("r14", Register::GetR14, Register::SetR14)
    .def_property_static("r14d", Register::GetR14D, Register::SetR14D)
    .def_property_static("r14w", Register::GetR14W, Register::SetR14W)
    .def_property_static("r14b", Register::GetR14B, Register::SetR14B)
    .def_property_static("r15", Register::GetR15, Register::SetR15)
    .def_property_static("r15d", Register::GetR15D, Register::SetR15D)
    .def_property_static("r15w", Register::GetR15W, Register::SetR15W)
    .def_property_static("r15b", Register::GetR15B, Register::SetR15B)
#endif //_WIN64

    .def_property_static("cax", Register::GetCAX, Register::SetCAX)
    .def_property_static("cbx", Register::GetCBX, Register::SetCBX)
    .def_property_static("ccx", Register::GetCCX, Register::SetCCX)
    .def_property_static("cdx", Register::GetCDX, Register::SetCDX)
    .def_property_static("cdi", Register::GetCDI, Register::SetCDI)
    .def_property_static("csi", Register::GetCSI, Register::SetCSI)
    .def_property_static("cbp", Register::GetCBP, Register::SetCBP)
    .def_property_static("csp", Register::GetCSP, Register::SetCSP)
    .def_property_static("cip", Register::GetCIP, Register::SetCIP);


    return m.ptr();

#undef arg
}