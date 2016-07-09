%module _scriptapi_gui
%{
#include "_scriptapi_gui.h"
%}

%rename(Gui_SelectionGet) Script::Gui::SelectionGet;
%rename(Gui_SelectionSet) Script::Gui::SelectionSet;
%rename(Gui_SelectionGetStart) Script::Gui::SelectionGetStart;
%rename(Gui_SelectionGetEnd) Script::Gui::SelectionGetEnd;

%rename(Disassembly_SelectionGet) Script::Gui::Disassembly::SelectionGet;
%rename(Disassembly_SelectionSet) Script::Gui::Disassembly::SelectionSet;
%rename(Disassembly_SelectionGetStart) Script::Gui::Disassembly::SelectionGetStart;
%rename(Disassembly_SelectionGetEnd) Script::Gui::Disassembly::SelectionGetEnd;

%rename(Dump_SelectionGet) Script::Gui::Dump::SelectionGet;
%rename(Dump_SelectionSet) Script::Gui::Dump::SelectionSet;
%rename(Dump_SelectionGetStart) Script::Gui::Dump::SelectionGetStart;
%rename(Dump_SelectionGetEnd) Script::Gui::Dump::SelectionGetEnd;

%rename(Stack_SelectionGet) Script::Gui::Stack::SelectionGet;
%rename(Stack_SelectionSet) Script::Gui::Stack::SelectionSet;
%rename(Stack_SelectionGetStart) Script::Gui::Stack::SelectionGetStart;
%rename(Stack_SelectionGetEnd) Script::Gui::Stack::SelectionGetEnd;

%apply duint *OUTPUT { duint *value };
%apply duint *OUTPUT { duint *start };
%apply duint *OUTPUT { duint *end };

%include "..\pluginsdk\_scriptapi_gui.h"
