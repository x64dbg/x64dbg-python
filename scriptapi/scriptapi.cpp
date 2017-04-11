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

PYBIND11_PLUGIN(scriptapi)
{
#define arg(x) py::arg(#x)

    py::module m("scriptapi", "Python module to wrap the x64dbg script api.");

    py::class_<PyMemory>(m, "memory")
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

    return m.ptr();

#undef arg
}