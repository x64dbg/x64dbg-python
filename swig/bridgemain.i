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

%include <windows.i>
#define DECLSPEC_ALIGN(x) __declspec(align(x))
%include "..\pluginsdk\bridgemain.h"