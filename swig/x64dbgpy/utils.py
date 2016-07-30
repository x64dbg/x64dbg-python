import sys
import runpy
import shlex
from os import path
from ctypes import *


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def __OpenFileDialog():
    MAX_PATH = 260
    OFN_PATHMUSTEXIST = 0x00000800
    OFN_FILEMUSTEXIST = 0x00001000

    class OPENFILENAME(Structure):
        _fields_ = (("lStructSize", c_int),
                    ("hwndOwner", c_int),
                    ("hInstance", c_int),
                    ("lpstrFilter", c_wchar_p),
                    ("lpstrCustomFilter", c_char_p),
                    ("nMaxCustFilter", c_int),
                    ("nFilterIndex", c_int),
                    ("lpstrFile", c_wchar_p),
                    ("nMaxFile", c_int),
                    ("lpstrFileTitle", c_wchar_p),
                    ("nMaxFileTitle", c_int),
                    ("lpstrInitialDir", c_wchar_p),
                    ("lpstrTitle", c_wchar_p),
                    ("flags", c_int),
                    ("nFileOffset", c_ushort),
                    ("nFileExtension", c_ushort),
                    ("lpstrDefExt", c_char_p),
                    ("lCustData", c_int),
                    ("lpfnHook", c_char_p),
                    ("lpTemplateName", c_char_p),
                    ("pvReserved", c_char_p),
                    ("dwReserved", c_int),
                    ("flagsEx", c_int))

    opath = create_unicode_buffer(MAX_PATH)

    ofx = OPENFILENAME()
    ofx.lStructSize = sizeof(OPENFILENAME)
    ofx.nMaxFile = MAX_PATH
    ofx.hwndOwner = 0
    ofx.lpstrTitle = u"Select script file..."
    ofx.lpstrFile = cast(opath, c_wchar_p)
    ofx.lpstrFilter = u"Python files (*.py; *.pyw)\0*.py; *.pyw\0\0"
    ofx.flags = OFN_PATHMUSTEXIST | OFN_FILEMUSTEXIST
    is_ok = windll.comdlg32.GetOpenFileNameW(byref(ofx))
    if is_ok:
        return opath.value


def is_64bit():
    return sys.maxsize > 2**32


def open_python_file(run_file=False):
    file_path = __OpenFileDialog()
    if not file_path:
        return

    if run_file:
        sys.path.insert(0, path.dirname(file_path))
        runpy.run_path(
            path_name=file_path,
            init_globals=globals(),
            run_name='__main__',
        )

    return file_path


def get_plugins_dir():
    current_dir = path.dirname(__file__)
    return path.dirname(current_dir)


def x64dbg_pip(args=list()):
    try:
        import pip
        # Split arguments
        arg_list = shlex.split(args, comments=False, posix=False)
        return pip.main(args=arg_list[1:])
    except ImportError:
        print "Pip is not installed: Please install pip from 'https://pip.readthedocs.org/en/stable/installing/'"
