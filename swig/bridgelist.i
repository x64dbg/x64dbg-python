%module bridgemain
%{
#include "bridgelist.h"
%}

%include "..\pluginsdk\bridgelist.h"

%include "std_vector.i"

%define %ListInfo_func(TYPE,NAME)

%template(vector##NAME) std::vector<TYPE>;

%inline %{
std::vector<TYPE> NAME(ListInfo* l)
{
    std::vector<TYPE> vec(
        (TYPE*)l->data,
        (TYPE*)((byte*)l->data + l->size));
    BridgeFree(l->data);
    return vec;
}
%}

%enddef
