%module _scriptapi_argument
%{
#include "_scriptapi_argument.h"
%}

%rename(Argument_Add) Script::Argument::Add;
%rename(Argument_Get) Script::Argument::Get;
%rename(Argument_GetInfo) Script::Argument::GetInfo;
%rename(Argument_Overlaps) Script::Argument::Overlaps;
%rename(Argument_Delete) Script::Argument::Delete;
%rename(Argument_DeleteRange) Script::Argument::DeleteRange;
%rename(Argument_Clear) Script::Argument::Clear;
%rename(Argument_GetList) Script::Argument::GetList;

%apply duint *INOUT { duint *start };
%apply duint *INOUT { duint *end };
%apply duint *INOUT { duint *instructionCount };

%include "..\pluginsdk\_scriptapi_argument.h"

%ListInfo_func(Script::Argument::ArgumentInfo,GetArgumentInfoList)
