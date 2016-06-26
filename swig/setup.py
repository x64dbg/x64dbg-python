#!/usr/bin/env python
import sys
from distutils.core import setup, Extension
from distutils.command.build import build


def is_64bit():
    return sys.maxsize > 2 ** 32


class SwigBuild(build):
    def run(self):
        self.run_command('build_ext')
        build.run(self)


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
        r'x64dbg_python.pluginsdk._x64dbg', [r'x64dbg.i'],
        swig_opts=['-Wall', '-c++', '-outputtuple',
                   '-outdir', r'x64dbg_python\pluginsdk',
                   '-D"_WIN64"' if is_64bit() else ''],
        language='c++',
        include_dirs=[r'..\pluginsdk', r'include'],
        library_dirs=[r'..\pluginsdk'],
        libraries=['x64bridge', 'x64dbg'] if is_64bit() else ['x32bridge', 'x32dbg'],
        extra_compile_args=['/EHsc'],
    )],
    py_modules=['x64dbg_python.pluginsdk.x64dbg'],
    cmdclass={'build': SwigBuild},
)
