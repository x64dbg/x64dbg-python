import sys
# import runpy
# import tkFileDialog
# from Tkinter import Tk
# import os
# from os import path


def is_64bit():
    return sys.maxsize > 2**32


# def open_python_file(run_file=True):
#     root = Tk()
#     root.withdraw()
#
#     file_opt = {
#         'defaultextension': '*.py;*.pyw',
#         'filetypes': [('Python files', '*.py;*.pyw')],
#         'parent': root,
#         'title': 'Select script file...',
#     }
#
#     file_path = tkFileDialog.askopenfilename(**file_opt)
#     if not file_path:
#         return
#
#     if run_file:
#         old_path = os.getcwdu()
#         os.chdir(path.dirname(file_path))
#         runpy.run_path(
#             path_name=file_path,
#             run_name='__main__',
#         )
#         os.chdir(old_path)
#
#     root.destroy()
#     return file_path
