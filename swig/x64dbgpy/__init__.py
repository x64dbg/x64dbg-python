__author__ = 'Tomer Zait (RealGame)'
__version__ = '1.0.0'

import hooks
import pluginsdk
import __registers
import __events
import __flags
import __breakpoints

Register = __registers.Register()
Event = __events.Event()
Flag = __flags.Flag()
Breakpoint = __breakpoints.Breakpoint(Event)
