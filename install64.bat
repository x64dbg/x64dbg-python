@echo off

set PLUGINDIR=%~dp0\..\x64_dbg\bin\x64\plugins
mkdir %PLUGINDIR%
copy bin\x64\x64dbg-python.dll %PLUGINDIR%\x64dbg_python.dp64

call "%~dp0\setenv.bat"
@cd swig
"%PYTHON27X64%\python.exe" setup.py  install --install-lib="%PLUGINDIR%"
@cd ..

@echo on