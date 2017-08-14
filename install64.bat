@echo off

set RELEASEDIR=%~dp0release
set PLUGINDIR="%RELEASEDIR%\x64\plugins"
mkdir %PLUGINDIR%
copy bin\x64\x64dbgpy.dp64 %PLUGINDIR%\
copy bin\x64\x64dbgpy.lib %RELEASEDIR%\x64dbgpy_x64.lib
copy x64dbgpy.h %RELEASEDIR%\

@cd swig
call clean.bat
call "%~dp0\setenv.bat"
call %VCVARS% x86_amd64
set PYTHONHOME=%PYTHON27X64%
"%PYTHON27X64%\python.exe" setup.py  install --install-lib=%PLUGINDIR%\x64dbgpy
@cd ..

copy bin\x64\scriptapi.pyd %PLUGINDIR%\x64dbgpy\

@echo on