@echo off

set MSSDK=1
set DISTUTILS_USE_SDK=1
set VCVARS="%LOCALAPPDATA%\Programs\Common\Microsoft\Visual C++ for Python\9.0\vcvarsall.bat"
	
IF EXIST "%PROGRAMFILES(X86)%" (
    FOR /f "tokens=3" %%x IN ('reg query HKLM\SOFTWARE\Wow6432Node\Python\PythonCore\2.7\InstallPath /ve') DO (
        set PYTHON27X86=%%x
        setx PYTHON27X86 %%x
    )
    
    FOR /f "tokens=3" %%x IN ('reg query HKLM\SOFTWARE\Python\PythonCore\2.7\InstallPath /ve') DO (
        set PYTHON27X64=%%x
        setx PYTHON27X64 %%x
    )
) ELSE (
    FOR /f "tokens=3" %%x IN ('reg query HKLM\SOFTWARE\Python\PythonCore\2.7\InstallPath /ve') DO (
        set PYTHON27X86=%%x
        setx PYTHON27X86 %%x
    )
)

@echo on