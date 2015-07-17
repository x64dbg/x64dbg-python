%module _scriptapi
%{
#include "_scriptapi_assembler.h"
%}

// Type Maps
%pybuffer_string(char *error);
%pybuffer_string(unsigned char *dest)

%apply int *OUTPUT { int *size };

%include "..\pluginsdk\_scriptapi_assembler.h"
