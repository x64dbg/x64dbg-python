%module _scriptapi_pattern
%{
#include "_scriptapi_pattern.h"
%}

%pybuffer_mutable_binary(unsigned char* data, duint datasize)

%include "..\pluginsdk\_scriptapi_pattern.h"
