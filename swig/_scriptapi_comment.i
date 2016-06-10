%module _scriptapi_comment
%{
#include "_scriptapi_comment.h"
%}

%rename(Comment_Get) Script::Comment::Get;
%rename(Comment_Set) Script::Comment::Set;
%rename(Comment_GetInfo) Script::Comment::GetInfo;
%rename(Comment_Delete) Script::Comment::Delete;
%rename(Comment_DeleteRange) Script::Comment::DeleteRange;
%rename(Comment_DeleteRange) Script::Comment::DeleteRange;
%rename(Comment_Clear) Script::Comment::Clear;
%rename(Comment_GetList) Script::Comment::GetList;

%include "..\pluginsdk\_scriptapi_comment.h"

%ListInfo_func(Script::Comment::CommentInfo,GetCommentInfoList)
