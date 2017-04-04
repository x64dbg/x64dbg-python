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
    name='x64dbgpy',
    version='1.0',
    description='Python x64dbg SDK Library',
    author='Tomer Zait (RealGame)',
    author_email='realgam3@gmail.com',
    packages=[
        'x64dbgpy',
        'x64dbgpy.pluginsdk',
        'x64dbgpy.pluginsdk._scriptapi'
    ],
    package_data={
        'x64dbgpy': ['autorun/*']
    },
    ext_modules=[Extension(
        r'x64dbgpy.pluginsdk._x64dbg', [r'x64dbg.i'],
        swig_opts=['-Wall', '-c++', '-outputtuple',
                   '-outdir', r'x64dbgpy\pluginsdk',
                   '-D"_WIN64"' if is_64bit() else ''],
        language='c++',
        include_dirs=[r'..\pluginsdk', r'include'],
        library_dirs=[r'..\pluginsdk'],
        libraries=['x64bridge', 'x64dbg'] if is_64bit() else ['x32bridge', 'x32dbg'],
        extra_compile_args=['/EHsc', '/MT'],
    )],
    py_modules=['x64dbgpy.pluginsdk.x64dbg'],
    cmdclass={'build': SwigBuild},
)
