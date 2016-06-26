#ifndef _PY_H
#define _PY_H

#include "pluginmain.h"

extern HINSTANCE hInst;

//menu identifiers
#define MENU_OPEN 0
#define MENU_ABOUT 1

//functions
bool pyInit(PLUG_INITSTRUCT* initStruct);
void pyStop();
void pySetup();

#endif // _PY_H
