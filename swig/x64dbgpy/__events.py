# import os
# from os import path
# import runpy
# import glob
from utils import Singleton

EVENTS = [
    # 'init_debug',
    'stop_debug',
    'breakpoint',
    'create_process',
    'exit_process',
    'create_thread',
    'exit_thread',
    'system_breakpoint',
    'load_dll',
    'unload_dll',
]

class Event(object):
    __metaclass__ = Singleton

    def __init__(self):
        # Keys: type, addr, enabled, singleshoot, active, name, mod, slot
        # typedef struct
        # {
        #     BPXTYPE type;
        #     duint addr;
        #     bool enabled;
        #     bool singleshoot;
        #     bool active;
        #     char name[MAX_BREAKPOINT_SIZE];
        #     char mod[MAX_MODULE_SIZE];
        #     unsigned short slot;
        # } BRIDGEBP;
        #
        # typedef enum
        # {
        #     bp_none = 0,
        #     bp_normal = 1,
        #     bp_hardware = 2,
        #     bp_memory = 4
        # } BPXTYPE;
        self.breakpoint = None
        # Keys: None
        self.stop_debug = None
        # Keys: CreateProcessInfo, modInfo, DebugFileName, fdProcessInfo
        # typedef struct
        # {
        #     CREATE_PROCESS_DEBUG_INFO* CreateProcessInfo;
        #     IMAGEHLP_MODULE64* modInfo;
        #     const char* DebugFileName;
        #     PROCESS_INFORMATION* fdProcessInfo;
        # } PLUG_CB_CREATEPROCESS;
        self.create_process = None
        # Keys: dwExitCode
        # typedef struct _EXIT_PROCESS_DEBUG_INFO {
        #   DWORD dwExitCode;
        # } EXIT_PROCESS_DEBUG_INFO, *LPEXIT_PROCESS_DEBUG_INFO;
        self.exit_process = None
        # Keys: CreateThread, dwThreadId
        # typedef struct
        # {
        #     CREATE_THREAD_DEBUG_INFO* CreateThread;
        #     DWORD dwThreadId;
        # } PLUG_CB_CREATETHREAD;
        self.create_thread = None
        # Keys: dwThreadId, dwExitCode
        # typedef struct
        # {
        #     EXIT_THREAD_DEBUG_INFO* ExitThread;
        #     DWORD dwThreadId;
        # } PLUG_CB_EXITTHREAD;
        self.exit_thread = None
        # Keys: None
        self.system_breakpoint = None
        # Keys: LoadDll, modInfo, modname
        # typedef LoadDll, modInfo, modname
        # {
        #     LOAD_DLL_DEBUG_INFO* LoadDll;
        #     IMAGEHLP_MODULE64* modInfo;
        #     const char* modname;
        # } PLUG_CB_LOADDLL;
        self.load_dll = None
        # Keys: lpBaseOfDll
        # typedef struct
        # {
        #     UNLOAD_DLL_DEBUG_INFO* UnloadDll;
        # } PLUG_CB_UNLOADDLL;
        self.unload_dll = None

    def listen(self, event_name, callback):
        """
        Listen to event with a callback,
        Callback should always get key word arguments(kwargs).

        For example:
        def callback(**kwargs):
            print kwargs
        """
        event_name_lower = event_name.lower()
        if event_name_lower not in EVENTS:
            raise Exception("%s Is not a valid event." % event_name_lower)

        setattr(self, event_name_lower, callback)

    # @staticmethod
    # def init_debug():
    #     old_path = os.getcwdu()
    #     os.chdir(path.join(path.dirname(__file__), 'autorun'))
    #     for file_path in glob.glob("*.py"):
    #         print "[PYTHON] Executing autorun file: '%s'." % file_path
    #         runpy.run_path(
    #             path_name=file_path,
    #             run_name='__main__',
    #         )
    #         os.chdir(old_path)
