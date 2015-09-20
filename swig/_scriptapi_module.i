%module _scriptapi_module
%{
#include "_scriptapi_module.h"
%}

// Type Maps
%include <pybuffer.i>
%pybuffer_string(char* name);
%pybuffer_string(char* path);

%include "..\pluginsdk\_scriptapi_module.h"
