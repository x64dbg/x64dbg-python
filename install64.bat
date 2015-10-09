@echo off

set PLUGINDIR=%~dp0\release\x64\plugins
mkdir %PLUGINDIR%
copy bin\x64\x64dbg-python.dll %PLUGINDIR%\x64dbg_python.dp64

@cd swig
call "%~dp0\setenv.bat"
call %VCVARS% x86_amd64
"%PYTHON27X64%\python.exe" setup.py  install --install-lib="%PLUGINDIR%"
@cd ..

@echo on