import win32gui
import win32process
import psutil, os
from datetime import datetime
import time
import ctypes
import ctypes.wintypes as wintypes

is_app_running = True
stop_run = False
def main():
    print("Main")

    
EVENT_SYSTEM_FOREGROUND = 0x0003
WINEVENT_OUTOFCONTEXT = 0x0000

# 1. Describe the shape of the callback: returns nothing, takes these 7 args
WinEventProcType = ctypes.WINFUNCTYPE(
    None,
    wintypes.HANDLE,  # hWinEventHook
    wintypes.DWORD,   # event
    wintypes.HWND,    # hwnd
    wintypes.LONG,    # idObject
    wintypes.LONG,    # idChild
    wintypes.DWORD,   # idEventThread
    wintypes.DWORD,   # dwmsEventTime
)

# 2. Your function. Windows calls it, you never do.
def my_callback(hWinEventHook, event, hwnd, idObject, idChild, idEventThread, dwmsEventTime):
    print("App switch")

# 3. Wrap it, and keep it in a variable so Python doesn't garbage-collect it
callback = WinEventProcType(my_callback)

# 4. Register ("leave your phone number"). This returns immediately.
hook = ctypes.windll.user32.SetWinEventHook(
    EVENT_SYSTEM_FOREGROUND,   # eventMin
    EVENT_SYSTEM_FOREGROUND,   # eventMax
    0,                         # no module handle
    callback,                  # <- the function Windows calls later
    0, 0,                      # all processes, all threads
    WINEVENT_OUTOFCONTEXT,
)

print("Hook installed. Switch between windows...")

# 5. Wait here. Windows delivers events while this blocks.
win32gui.PumpMessages()

        
        
    




def check_running_apps():
    #get all the running processes
    return apps

def check_active_window_processid():
    current_active = "" #declare so it has a base 
    while not stop_run: #global declaration
        try:
            hwnd = win32gui.GetForegroundWindow()
            if not hwnd:
                pass
            else:
                tid, pid = win32process.GetWindowThreadProcessId(hwnd)
                process_name = psutil.Process(pid)
                
                if process_name != current_active: 
                    
                    current_time = datetime.now()
                    applogs(win32gui.GetWindowText(hwnd), process_name, current_time)

                    #change current.
                    current_active = process_name
            time.sleep(1)
        except KeyError as e:
            print("Error:", e)
    ctypes.windll.user32
        
        


        

def applogs(app_name, process_name, current_time):
    #log the active window and time spent
    
    #logs.txt write (appname, processname, current time)
    return 


def running(app_is_running):
    while app_is_running:
        current_time = datetime.now()

if __name__ == "__main__":
    main()
