%module _scriptapi
%{
#include <windows.h>
#include "_scriptapi.h"
%}

%include <windows.i>
%include "..\pluginsdk\_scriptapi.h"

%include "_scriptapi_debug.i"
%include "_scriptapi_memory.i"
%include "_scriptapi_register.i"
%include "_scriptapi_pattern.i"
%include "_scriptapi_gui.i"
%include "_scriptapi_misc.i"
%include "_scriptapi_stack.i"
%include "_scriptapi_assembler.i"
%include "_scriptapi_module.i"
%include "_scriptapi_flag.i"
