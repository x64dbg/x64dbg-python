# x64dbg-python
Automating x64dbg using Python

Works with: snapshot_2016-03-21_09-55
https://sourceforge.net/projects/x64dbg/files/snapshots/snapshot_2016-03-21_09-55.7z/download


### To develop you will need:
1) Visual Studio 2015 Community: https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx <br />
2) Python 2.7 x64 + x86 && pip (Python 2.7.10 has pip on it) - https://www.python.org/downloads/release/python-2710/ <br />
3) Microsoft Visual C++ Compiler for Python 2.7: http://www.microsoft.com/en-us/download/details.aspx?id=44266 <br />
4) PyCharm Community Edition (If you are python developer) : https://www.jetbrains.com/pycharm/download/

### To install and test:
1) Install Python 2.7.10 (x64 + x86) In seperate folders. <br />
2) Install Visual Studio 2015 Community. <br />
3) Open setenv.bat from the project folder. <br />
4) Compile the win32 and win64 dlls. <br />
5) Copy the release folder from the snapshot to the project directory. <br />
6) Run install32.bat and install64.bat. <br />

### Contributors:
1) Run install.bat (git hook for code buetify) <br />
2) Test your code <br />
3) Read PEP8: https://www.python.org/dev/peps/pep-0008/

### Example scripts:
* https://github.com/realgam3/ReversingAutomation/tree/master/X64dbg-Python

### Help:
* I need help with the swig / cpp development,
* Translating the event callbacks to swig and use it without the code in py.cpp file.
* Connecting ipython interpreter to x64dbg-python.
* Python multiprocessing with x64dbg-python plugin (Python embedded).