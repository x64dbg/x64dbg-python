@echo off

set PLUGINDIR=%~dp0\release\x32\plugins
mkdir %PLUGINDIR%
mkdir %PLUGINDIR%\X64Dbg_editor

copy bin\x32\x64dbg-python.dll X64Dbg_editor\x64dbg_python.dp32
xcopy /e /c /y swig\build\lib.win32-2.7\x64dbg_python %PLUGINDIR%\x64dbg_python\
copy swig\PyQt-win-gpl-4.11.4-x64dbg-edition-download.py %PLUGINDIR%\PyQt-win-gpl-4.11.4-x64dbg-edition-download.py   
@cd swig
call "%~dp0\setenv.bat"
call %VCVARSX86%
"%PYTHON27X86%\python.exe" setup.py  install --install-lib="%PLUGINDIR%"
@cd %PLUGINDIR%
"%PYTHON27X86%\python.exe"  PyQt-win-gpl-4.11.4-x64dbg-edition-download.py
rename master.zip PyQt4_for_xdbg64_installer.zip
del PyQt-win-gpl-4.11.4-x64dbg-edition-download.py
@cd %~dp0
XCOPY 3party\X64Dbg_editor\* %PLUGINDIR%\X64Dbg_editor\ /s /i
@ echo remember to copy X64Dbg_editor folder to 64_dbg\bin\x32\plugins\X64Dbg_editor !
@ echo Remember to install the PyQt4 x64 bundle PyQt4_for_xdbg64_installer.zip !
@ pause

@echo on