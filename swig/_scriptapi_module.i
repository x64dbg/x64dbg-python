%module _scriptapi_module
%{
#include "_scriptapi_module.h"
%}

// Type Maps
%include <pybuffer.i>
%pybuffer_string(char* name);
%pybuffer_string(char* path);

%ListInfo_func(Script::Module::ModuleInfo,GetModuleInfoList)
%ListInfo_func(Script::Module::ModuleSectionInfo,GetModuleSectionInfoList)

%include "..\pluginsdk\_scriptapi_module.h"
