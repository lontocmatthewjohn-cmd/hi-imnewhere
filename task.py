import win32gui
import win32process
import psutil, os
from datetime import datetime
import time

is_app_running = True
stop_run = False
def main():
    starting_time = datetime.now()

    #when new/switching windows/process

    check_active_window_processid()

        
        
    





def check_running_apps():
    #get all the running processes
    return apps

def check_active_window_processid():
    current_active = "" #declare so it has a base 
    while not stop_run: #global declaration
        try:
            hwnd = win32gui.GetForegroundWindow()
            tid, pid = win32process.GetWindowThreadProcessId(hwnd)
            process_name = psutil.Process(pid)
            
            
            if process_name != current_active: 
                current_time = datetime.now()
                applogs(win32gui.GetWindowText(hwnd), process_name.name(), current_time)
                current_active = process_name


            time.sleep(1)
        except KeyError as e:
            print("Error:", e)

        


        

def applogs(app_name, process_name, current_time):
    #log the active window and time spent
    return applogs


def running(app_is_running):
    while app_is_running:
        current_time = datetime.now()

if __name__ == "__main__":
    main()
