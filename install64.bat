@echo off
set PLUGINDIR=..\x64_dbg\bin\x64\plugins
mkdir %PLUGINDIR%
copy bin\x64\x64dbg-python.dll %PLUGINDIR%\x64dbg_python.dp64

cd swig
call "%ProgramFiles(x86)%\Microsoft Visual Studio 9.0\VC\bin\x86_amd64\vcvarsx86_amd64.bat"
set MSSDK=1
set DISTUTILS_USE_SDK=1
for /f "tokens=3" %%x in ('reg query HKLM\SOFTWARE\Python\PythonCore\2.7\InstallPath /ve') do set PYTHONDIR=%%x
"%PYTHONDIR%python.exe" setup.py  install --install-lib="..\%PLUGINDIR%"
cd ..