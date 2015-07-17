swig -Wall -c++ -python -outputtuple  -D"_WIN64" -outdir x64dbg_python\pluginsdk -o x64dbg_python\pluginsdk\_x64dbg.cpp x64dbg.i
python setup.py build