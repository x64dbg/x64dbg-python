from . import x64dbg

def _encode(text):
    try:
        return text.encode()
    except Exception:
        return repr(text)


def _plugin_logprint(text=''):
    x64dbg._plugin_logprint(_encode(text))


def _plugin_logputs(text=''):
    x64dbg._plugin_logputs(_encode(text))
