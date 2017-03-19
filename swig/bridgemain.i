%module bridgemain
%{
#include "bridgemain.h"
#define nullptr 0
%}

// Allow Python Buffers
%include <pybuffer.i>

// Type Maps
%pybuffer_string(char* text);

%typemap(out) HWND {
    $result = PyInt_FromLong((long)$1);
}

%include "std_vector.i"

%template(ThreadVector) std::vector<THREADALLINFO>;

%inline %{
std::vector<THREADALLINFO> GetThreadInfoList(THREADLIST* l)
{
    std::vector<THREADALLINFO> vec(
        l->list,
        l->list + l->count
    );
    BridgeFree(l->list);
    return vec;
}
%}

%include <windows.i>
#define DECLSPEC_ALIGN(x) __declspec(align(x))
%include "..\pluginsdk\bridgemain.h"