%module _scriptapi_label
%{
#include "_scriptapi_label.h"
%}

%rename(Label_Get) Script::Label::Get;
%rename(Label_Set) Script::Label::Set;
%rename(Label_GetInfo) Script::Label::GetInfo;
%rename(Label_Delete) Script::Label::Delete;
%rename(Label_DeleteRange) Script::Label::DeleteRange;
%rename(Label_Clear) Script::Label::Clear;
%rename(Label_GetList) Script::Label::GetList;

%apply duint *OUTPUT { duint *addr };

%include "..\pluginsdk\_scriptapi_label.h"

%ListInfo_func(Script::Label::LabelInfo,GetLabelInfoList)
