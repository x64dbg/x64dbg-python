@echo off
call install32.bat
call install64.bat
xcopy release\* ..\x64dbg\bin\ /S /Y