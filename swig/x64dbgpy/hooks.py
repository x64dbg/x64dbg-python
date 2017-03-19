import sys
import signal
import warnings
import __builtin__
from os import path
import multiprocessing
from pluginsdk import bridgemain, _plugins


def __raw_input(prompt=''):
    return bridgemain.GuiGetLineWindow(prompt)


def __input(prompt=''):
    return eval(__raw_input(prompt))


def __signal(sig, action):
    warnings.warn('Cannot use signals in x64dbgpy...', UserWarning, stacklevel=2)


class OutputHook(object):
    def __init__(self, stream_name='stdout', callback=_plugins._plugin_logprint):
        self.is_hooking = False
        self.callback = callback

        self.stream_name = stream_name
        if self.stream_name not in ['stderr', 'stdout']:
            raise Exception('Cannot hook %s stream.' % self.stream_name)
        elif self.__is_hooked():
            raise Exception('Do not hook the hooker!')

        self.__original_stream = getattr(sys, self.stream_name)

    def __getattr__(self, name):
        return getattr(self.__original_stream, name)

    def __is_hooked(self):
        stream = getattr(sys, self.stream_name)
        return hasattr(stream, 'is_hooking')

    def write(self, text):
        self.callback(text)

    def start(self):
        if not self.is_hooking:
            setattr(sys, self.stream_name, self)
            self.is_hooking = True

    def stop(self):
        if self.is_hooking:
            setattr(sys, self.stream_name, self.__original_stream)
            self.is_hooking = False


# Hook sys.stdout
STDOUT_HOOK = OutputHook('stdout')
STDOUT_HOOK.start()

# Hook sys.stderr
STDERR_HOOK = OutputHook('stderr')
STDERR_HOOK.start()

# Hook raw_input, input (stdin)
setattr(__builtin__, 'original_raw_input', __builtin__.raw_input)
setattr(__builtin__, 'raw_input', __raw_input)
setattr(__builtin__, 'original_input', __builtin__.input)
setattr(__builtin__, 'input', __input)

# Set arguments
sys.argv = [path.join(path.dirname(__file__), '__init__.py')]

# Hook Signals (for pip and other signal based programs)
setattr(signal, 'original_signal', signal.signal)
setattr(signal, 'signal', __signal)

# Fix Multiprocessing (Will not be able to use x64dbgpy lib for now...)
multiprocessing.set_executable(path.join(sys.exec_prefix, 'pythonw.exe'))

# Print Message That The Hooks Worked!
print '[PYTHON] stdout, stderr, raw_input hooked!'
