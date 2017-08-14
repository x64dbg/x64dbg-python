#pragma warning(disable:4091)
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

struct PyDebugger
{
};

//https://stackoverflow.com/a/43526890/1806760
template <typename> struct FirstArgument;

template <typename R, typename A, typename... Args>
struct FirstArgument<R(A, Args...)>
{
    using type = A;
};

template <typename T>
using first_agument_t = typename FirstArgument<T>::type;

PYBIND11_PLUGIN(scriptapi)
{
#define arg(x) py::arg(#x)
#define pget(x) [](py::object) { return x(); }
#define pset(x) [](py::object, duint value) { return x(first_agument_t<decltype(x)>(value)); }

    py::module m("scriptapi", "Python module to wrap the x64dbg script api.");

    py::class_<PyMemory>(m, "Memory")
    .def(py::init<>()) //it's the pythonic way `mem = scriptapi.Memory()`
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
    .def(py::init<>()) //it's the pythonic way `regs = scriptapi.Registers()`
    .def_property_static("dr0", pget(Register::GetDR0), pset(Register::SetDR0))
    .def_property_static("dr1", pget(Register::GetDR1), pset(Register::SetDR1))
    .def_property_static("dr2", pget(Register::GetDR2), pset(Register::SetDR2))
    .def_property_static("dr3", pget(Register::GetDR3), pset(Register::SetDR3))
    .def_property_static("dr6", pget(Register::GetDR6), pset(Register::SetDR6))
    .def_property_static("dr7", pget(Register::GetDR7), pset(Register::SetDR7))

    .def_property_static("eax", pget(Register::GetEAX), pset(Register::SetEAX))
    .def_property_static("ax", pget(Register::GetAX), pset(Register::SetAX))
    .def_property_static("ah", pget(Register::GetAH), pset(Register::SetAH))
    .def_property_static("al", pget(Register::GetAL), pset(Register::SetAL))
    .def_property_static("ebx", pget(Register::GetEBX), pset(Register::SetEBX))
    .def_property_static("bx", pget(Register::GetBX), pset(Register::SetBX))
    .def_property_static("bh", pget(Register::GetBH), pset(Register::SetBH))
    .def_property_static("bl", pget(Register::GetBL), pset(Register::SetBL))
    .def_property_static("ecx", pget(Register::GetECX), pset(Register::SetECX))
    .def_property_static("cx", pget(Register::GetCX), pset(Register::SetCX))
    .def_property_static("ch", pget(Register::GetCH), pset(Register::SetCH))
    .def_property_static("cl", pget(Register::GetCL), pset(Register::SetCL))
    .def_property_static("edx", pget(Register::GetEDX), pset(Register::SetEDX))
    .def_property_static("dx", pget(Register::GetDX), pset(Register::SetDX))
    .def_property_static("dh", pget(Register::GetDH), pset(Register::SetDH))
    .def_property_static("dl", pget(Register::GetDL), pset(Register::SetDL))
    .def_property_static("edi", pget(Register::GetEDI), pset(Register::SetEDI))
    .def_property_static("di", pget(Register::GetDI), pset(Register::SetDI))
    .def_property_static("esi", pget(Register::GetESI), pset(Register::SetESI))
    .def_property_static("si", pget(Register::GetSI), pset(Register::SetSI))
    .def_property_static("ebp", pget(Register::GetEBP), pset(Register::SetEBP))
    .def_property_static("bp", pget(Register::GetBP), pset(Register::SetBP))
    .def_property_static("esp", pget(Register::GetESP), pset(Register::SetESP))
    .def_property_static("sp", pget(Register::GetSP), pset(Register::SetSP))
    .def_property_static("eip", pget(Register::GetEIP), pset(Register::SetEIP))
    .def_property_static("eflags", pget(Register::GetCFLAGS), pset(Register::SetCFLAGS))

#ifdef _WIN64
    .def_property_static("rax", pget(Register::GetRAX), pset(Register::SetRAX))
    .def_property_static("rbx", pget(Register::GetRBX), pset(Register::SetRBX))
    .def_property_static("rcx", pget(Register::GetRCX), pset(Register::SetRCX))
    .def_property_static("rdx", pget(Register::GetRDX), pset(Register::SetRDX))
    .def_property_static("rsi", pget(Register::GetRSI), pset(Register::SetRSI))
    .def_property_static("sil", pget(Register::GetSIL), pset(Register::SetSIL))
    .def_property_static("rdi", pget(Register::GetRDI), pset(Register::SetRDI))
    .def_property_static("dil", pget(Register::GetDIL), pset(Register::SetDIL))
    .def_property_static("rbp", pget(Register::GetRBP), pset(Register::SetRBP))
    .def_property_static("bpl", pget(Register::GetBPL), pset(Register::SetBPL))
    .def_property_static("rsp", pget(Register::GetRSP), pset(Register::SetRSP))
    .def_property_static("spl", pget(Register::GetSPL), pset(Register::SetSPL))
    .def_property_static("rip", pget(Register::GetRIP), pset(Register::SetRIP))
    .def_property_static("r8", pget(Register::GetR8), pset(Register::SetR8))
    .def_property_static("r8d", pget(Register::GetR8D), pset(Register::SetR8D))
    .def_property_static("r8w", pget(Register::GetR8W), pset(Register::SetR8W))
    .def_property_static("r8b", pget(Register::GetR8B), pset(Register::SetR8B))
    .def_property_static("r9", pget(Register::GetR9), pset(Register::SetR9))
    .def_property_static("r9d", pget(Register::GetR9D), pset(Register::SetR9D))
    .def_property_static("r9w", pget(Register::GetR9W), pset(Register::SetR9W))
    .def_property_static("r9b", pget(Register::GetR9B), pset(Register::SetR9B))
    .def_property_static("r10", pget(Register::GetR10), pset(Register::SetR10))
    .def_property_static("r10d", pget(Register::GetR10D), pset(Register::SetR10D))
    .def_property_static("r10w", pget(Register::GetR10W), pset(Register::SetR10W))
    .def_property_static("r10b", pget(Register::GetR10B), pset(Register::SetR10B))
    .def_property_static("r11", pget(Register::GetR11), pset(Register::SetR11))
    .def_property_static("r11d", pget(Register::GetR11D), pset(Register::SetR11D))
    .def_property_static("r11w", pget(Register::GetR11W), pset(Register::SetR11W))
    .def_property_static("r11b", pget(Register::GetR11B), pset(Register::SetR11B))
    .def_property_static("r12", pget(Register::GetR12), pset(Register::SetR12))
    .def_property_static("r12d", pget(Register::GetR12D), pset(Register::SetR12D))
    .def_property_static("r12w", pget(Register::GetR12W), pset(Register::SetR12W))
    .def_property_static("r12b", pget(Register::GetR12B), pset(Register::SetR12B))
    .def_property_static("r13", pget(Register::GetR13), pset(Register::SetR13))
    .def_property_static("r13d", pget(Register::GetR13D), pset(Register::SetR13D))
    .def_property_static("r13w", pget(Register::GetR13W), pset(Register::SetR13W))
    .def_property_static("r13b", pget(Register::GetR13B), pset(Register::SetR13B))
    .def_property_static("r14", pget(Register::GetR14), pset(Register::SetR14))
    .def_property_static("r14d", pget(Register::GetR14D), pset(Register::SetR14D))
    .def_property_static("r14w", pget(Register::GetR14W), pset(Register::SetR14W))
    .def_property_static("r14b", pget(Register::GetR14B), pset(Register::SetR14B))
    .def_property_static("r15", pget(Register::GetR15), pset(Register::SetR15))
    .def_property_static("r15d", pget(Register::GetR15D), pset(Register::SetR15D))
    .def_property_static("r15w", pget(Register::GetR15W), pset(Register::SetR15W))
    .def_property_static("r15b", pget(Register::GetR15B), pset(Register::SetR15B))
    .def_property_static("rflags", pget(Register::GetCFLAGS), pset(Register::SetCFLAGS))
#endif //_WIN64

    .def_property_static("cax", pget(Register::GetCAX), pset(Register::SetCAX))
    .def_property_static("cbx", pget(Register::GetCBX), pset(Register::SetCBX))
    .def_property_static("ccx", pget(Register::GetCCX), pset(Register::SetCCX))
    .def_property_static("cdx", pget(Register::GetCDX), pset(Register::SetCDX))
    .def_property_static("cdi", pget(Register::GetCDI), pset(Register::SetCDI))
    .def_property_static("csi", pget(Register::GetCSI), pset(Register::SetCSI))
    .def_property_static("cbp", pget(Register::GetCBP), pset(Register::SetCBP))
    .def_property_static("csp", pget(Register::GetCSP), pset(Register::SetCSP))
    .def_property_static("cip", pget(Register::GetCIP), pset(Register::SetCIP))
    .def_property_static("cflags", pget(Register::GetCFLAGS), pset(Register::SetCFLAGS));

    py::class_<PyDebugger>(m, "Debugger")
    .def(py::init<>());


    return m.ptr();
}