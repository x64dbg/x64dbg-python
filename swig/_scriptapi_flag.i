%module _scriptapi_flag
%{
#include "_scriptapi_flag.h"
%}

%rename(Flag_Get) Script::Flag::Get;
%rename(Flag_Set) Script::Flag::Set;

%include "..\pluginsdk\_scriptapi_flag.h"
