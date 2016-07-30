import functools
import pluginsdk._scriptapi
from utils import Singleton
from pluginsdk.bridgemain import GuiUpdateAllViews


FLAGS = (
    'ZF', 'OF', 'CF',
    'PF', 'SF', 'TF',
    'AF', 'DF', 'IF'
)


class Flag(object):
    __metaclass__ = Singleton

    def __init__(self, refresh_gui=True):
        self.refresh_gui = refresh_gui

        for flag in FLAGS:
            setattr(self.__class__, flag, property(
                fget=functools.partial(self._get_func, register=flag),
                fset=functools.partial(self._set_func, register=flag)
            ))

    @staticmethod
    def __get_flag_function(flag, get=True):
        flag_name = flag.upper()
        if flag_name not in FLAGS:
            raise Exception("'%s' is not a valid flag." % flag)

        return getattr(
            pluginsdk._scriptapi.flag,
            '{method}{flag}'.format(
                method='Get' if get else 'Set',
                flag=flag_name
            )
        )

    @staticmethod
    def _get_func(self, register):
        return self.__get_flag_function(register)()

    @staticmethod    
    def _set_func(self, value, flag):
        self.__get_flag_function(flag, get=False)(value)
        if self.refresh_gui:
            GuiUpdateAllViews()
