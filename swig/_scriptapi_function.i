%module _scriptapi_function
%{
#include "_scriptapi_function.h"
%}

%rename(Function_Add) Script::Function::Add;
%rename(Function_Get) Script::Function::Get;
%rename(Function_GetInfo) Script::Function::GetInfo;
%rename(Function_Overlaps) Script::Function::Overlaps;
%rename(Function_Delete) Script::Function::Delete;
%rename(Function_DeleteRange) Script::Function::DeleteRange;
%rename(Function_Clear) Script::Function::Clear;
%rename(Function_GetList) Script::Function::GetList;

%include "..\pluginsdk\_scriptapi_function.h"

%ListInfo_func(Script::Function::FunctionInfo,GetFunctionInfoList)
