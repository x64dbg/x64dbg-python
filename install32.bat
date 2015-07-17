@echo off
set PLUGINDIR=..\x64_dbg\bin\x32\plugins
mkdir %PLUGINDIR%
copy bin\x32\x64dbg-python.dll %PLUGINDIR%\x64dbg_python.dp32

cd swig
set MSSDK=1
set DISTUTILS_USE_SDK=1
IF EXIST "%PROGRAMFILES(X86)%" (
    call "%ProgramFiles(x86)%\Microsoft Visual Studio 9.0\VC\bin\vcvars32.bat"
    for /f "tokens=3" %%x in ('reg query HKLM\SOFTWARE\Wow6432Node\Python\PythonCore\2.7\InstallPath /ve') do set PYTHONDIR=%%x
) ELSE (
    call "%ProgramFiles%\Microsoft Visual Studio 9.0\VC\bin\vcvars32.bat"
    for /f "tokens=3" %%x in ('reg query HKLM\SOFTWARE\Python\PythonCore\2.7\InstallPath /ve') do set PYTHONDIR=%%x
)
"%PYTHONDIR%python.exe" setup.py  install --install-lib="..\%PLUGINDIR%"
cd ..