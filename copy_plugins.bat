@echo off
call install32.bat
call install64.bat
xcopy release\x32\* ..\x64dbg\bin\x32\ /S /Y
xcopy release\x64\* ..\x64dbg\bin\x64\ /S /Y