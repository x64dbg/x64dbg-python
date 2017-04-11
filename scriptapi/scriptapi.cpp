#include <windows.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

static int add(int a, int b)
{
    return a + b;
}

PYBIND11_PLUGIN(scriptapi)
{
    py::module m("scriptapi", "Python module to wrap the x64dbg script api.");

    m.def("add", &add, "A function that adds two numbers.");

    return m.ptr();
}