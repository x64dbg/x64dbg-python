%module _scriptapi_pattern
%{
#include "_scriptapi_pattern.h"
%}

%pybuffer_mutable_binary(unsigned char* data, duint datasize)

%rename(Pattern_Write) Script::Pattern::Write;
%rename(Pattern_WriteMem) Script::Pattern::WriteMem;

%include "..\pluginsdk\_scriptapi_pattern.h"
