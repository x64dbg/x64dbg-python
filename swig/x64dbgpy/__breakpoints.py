from collections import defaultdict
from utils import Singleton
from pluginsdk._scriptapi.debug import SetBreakpoint, DeleteBreakpoint, \
    SetHardwareBreakpoint, DeleteHardwareBreakpoint, HardwareType

NONE = 0
NORMAL = 1
HARDWARE = 2
MEMORY = 4

ACCESS = HardwareType.HardwareAccess
WRITE = HardwareType.HardwareWrite
EXECUTE = HardwareType.HardwareExecute


class Breakpoint(object):
    __metaclass__ = Singleton

    BP_NONE = NONE
    BP_NORMAL = NORMAL
    BP_HARDWARE = HARDWARE
    BP_MEMORY = MEMORY

    HW_ACCESS = ACCESS
    HW_WRITE = WRITE
    HW_EXECUTE = EXECUTE

    def __init__(self, event_object):
        self.__breakpoints = defaultdict(dict)
        self.__event_object = event_object

        self.enable()

    def __breakpoint_function(self, **kwargs):
        address = kwargs['addr']
        if address in self.__breakpoints:
            if not (kwargs['enabled'] and kwargs['active']):
                return

            arg_keys = self.__breakpoints[address]['callback_args']
            self.__breakpoints[address]['callback'](
                **{key: value for key, value in kwargs.iteritems() if key in arg_keys}
            )

    def enable(self):
        self.__event_object.listen('breakpoint', self.__breakpoint_function)

    def disable(self):
        self.__event_object.listen('breakpoint', None)

    def add(self, address, callback, bp_type=NORMAL, hw_type=EXECUTE, callback_args=()):
        if bp_type == self.BP_NORMAL:
            SetBreakpoint(address)
        elif bp_type == self.BP_HARDWARE:
            SetHardwareBreakpoint(address, hw_type)

        self.__breakpoints[address]['callback'] = callback
        self.__breakpoints[address]['type'] = bp_type
        self.__breakpoints[address]['callback_args'] = callback_args

    def remove(self, address):
        if address not in self.__breakpoints:
            return

        bp_type = self.__breakpoints[address]['type']
        if bp_type == self.BP_NORMAL:
            DeleteBreakpoint(address)
        elif bp_type == self.BP_HARDWARE:
            DeleteHardwareBreakpoint(address)

        del self.__breakpoints[address]

    def list(self):
        return self.__breakpoints.keys()
