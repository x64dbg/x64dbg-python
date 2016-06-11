%module _scriptapi_symbol
%{
#include "_scriptapi_symbol.h"
%}

%rename(Symbol_GetList) Script::Symbol::GetList;

%include "..\pluginsdk\_scriptapi_symbol.h"

%ListInfo_func(Script::Symbol::SymbolInfo,GetSymbolInfoList)
