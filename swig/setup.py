#!/usr/bin/env python
import sys
from distutils.core import setup, Extension


def is_64bit():
    return sys.maxsize > 2 ** 32


setup(
    name='x64dbg_python',
    version='1.0',
    description='Python x64dbg SDK Library',
    author='Tomer Zait (RealGame)',
    author_email='realgam3@gmail.com',
    packages=[
        'x64dbg_python',
        'x64dbg_python.pluginsdk',
        'x64dbg_python.pluginsdk._scriptapi',
    ],
    package_data={'x64dbg_python': ['autorun/*']},
    ext_modules=[Extension(
        r'x64dbg_python.pluginsdk._x64dbg', [r'x64dbg_python\pluginsdk\_x64dbg.cpp'],
        language='c++',
        include_dirs=[r'..\pluginsdk'],
        library_dirs=[r'..\pluginsdk'],
        libraries=['x64bridge', 'x64dbg'] if is_64bit() else ['x32bridge', 'x32dbg'],
        extra_compile_args=['/EHsc'],
    )],
)
