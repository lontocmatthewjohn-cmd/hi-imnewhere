import win32gui, win32api, win32con
import win32process
import psutil, os
from datetime import datetime
import time
import ctypes
import ctypes.wintypes as wintypes
import threading
# i am using claude ai for guidance, but i am still writing it. its mostly because i dont want to read the documentation so i just ask it what each function to use/do. 
    
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
    if hwnd == 0:
        print("Error hwnd")
    else:
        try:
            current_time = datetime.now()
            app_title = win32gui.GetWindowText(hwnd)
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process_name = psutil.Process(pid)
            applogs(app_title, pid, process_name.name(), current_time)

        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            print("Error:", e)



def create_currentdaylog(): #create on start of program
    day = datetime.now().date()
    global currentday 
    currentday = f"{day}.txt" 
    try:
        with open(currentday, "a", encoding="utf-8") as file: 
            file.write(f"\n=========================\nDate: {day}")
            file.write(f"\n\tapp_title\t|\tpid\t|\tprocess_id\t|\tcurrent_time") 
    except OSError as e:
        print("There's an error: ", e)


def applogs(app_title, pid, process_id, current_time):
    exists(currentday) #doesnt return anything but if no file is found it will create instead.
    with open(currentday, "a", encoding="utf-8") as f:
        f.write(f"\n\t{app_title}\t|\t{pid}\t|\t{process_id}\t|\t{current_time}") 


def exists(path_currentday):
    if os.path.exists(path_currentday):
        print("File found, proceeding...")
    else:
        print("File not found, creating a new log file...")
        create_currentdaylog




def listen_for_quit():
    main_thread_id = win32api.GetCurrentThreadId()
    listener = input("Enter Q to quit")
    if listener:
        win32api.PostThreadMessage(main_thread_id, win32con.WM_QUIT, 0, 0)







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

create_currentdaylog()

threading.Thread(target=listen_for_quit, daemon=True).start()

# 5. Wait here. Windows delivers events while this blocks.
win32gui.PumpMessages()
        





        