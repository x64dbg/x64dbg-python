%module _scriptapi
%{
#include "_scriptapi_memory.h"
%}

// Type Maps
%include <pybuffer.i>
%pybuffer_string(void* data);
%apply duint *OUTPUT { duint *sizeRead };
%apply duint *OUTPUT { duint *sizeWritten };
%pybuffer_binary(parm, size_parm)

%rename(Memory_Read) Script::Memory::Read;
%rename(Memory_Write) Script::Memory::Write;

%include "..\pluginsdk\_scriptapi_memory.h"
