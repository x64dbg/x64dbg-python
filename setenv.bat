@echo off

set MSSDK=1
set DISTUTILS_USE_SDK=1

IF EXIST "%PROGRAMFILES(X86)%" (
    call "%ProgramFiles(x86)%\Microsoft Visual Studio 9.0\VC\bin\vcvars32.bat"
    FOR /f "tokens=3" %%x IN ('reg query HKLM\SOFTWARE\Wow6432Node\Python\PythonCore\2.7\InstallPath /ve') DO (
        set PYTHON27X86=%%x
        setx PYTHON27X86 %%x
    )
    
    call "%ProgramFiles(x86)%\Microsoft Visual Studio 9.0\VC\bin\x86_amd64\vcvarsx86_amd64.bat"
    FOR /f "tokens=3" %%x IN ('reg query HKLM\SOFTWARE\Python\PythonCore\2.7\InstallPath /ve') DO (
        set PYTHON27X64=%%x
        setx PYTHON27X64 %%x
    )
) ELSE (
    call "%ProgramFiles%\Microsoft Visual Studio 9.0\VC\bin\vcvars32.bat"
    FOR /f "tokens=3" %%x IN ('reg query HKLM\SOFTWARE\Python\PythonCore\2.7\InstallPath /ve') DO (
        set PYTHON27X86=%%x
        setx PYTHON27X86 %%x
    )
)

@echo on