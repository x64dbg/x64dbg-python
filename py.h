#ifndef _PY_H
#define _PY_H

#include "pluginmain.h"

extern HINSTANCE hInst;

//functions
bool pyInit(PLUG_INITSTRUCT* initStruct);
void pyStop();
void pySetup();

#endif // _PY_H
