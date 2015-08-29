@echo off

set PLUGINDIR=%~dp0\..\x64_dbg\bin\x32\plugins
mkdir %PLUGINDIR%
copy bin\x32\x64dbg-python.dll %PLUGINDIR%\x64dbg_python.dp32

call "%~dp0\setenv.bat"
@cd swig
"%PYTHON27X86%\python.exe" setup.py  install --install-lib="%PLUGINDIR%"
@cd ..

@echo on