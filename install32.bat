@echo off

set RELEASEDIR=%~dp0release
set PLUGINDIR="%RELEASEDIR%\x32\plugins"
mkdir %PLUGINDIR%
copy bin\x32\x64dbgpy.dp32 %PLUGINDIR%\
copy bin\x32\x64dbgpy.lib %RELEASEDIR%\x64dbgpy_x86.lib
copy x64dbgpy.h %RELEASEDIR%\

@cd swig
call clean.bat
call "%~dp0\setenv.bat"
call %VCVARS% x86
set PYTHONHOME=%PYTHON27X86%
"%PYTHON27X86%\python.exe" setup.py  install --install-lib=%PLUGINDIR%\x64dbgpy
@cd ..

copy bin\x32\scriptapi.pyd %PLUGINDIR%\x64dbgpy\

@echo on