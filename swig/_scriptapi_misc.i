%module _scriptapi_misc
%{
#include "_scriptapi_misc.h"
%}

%apply duint *OUTPUT { duint *value };

%include "..\pluginsdk\_scriptapi_misc.h"
