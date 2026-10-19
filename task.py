import win32gui as pywin
import psutil, os
from datetime import datetime

app_is_running = True

starting_time = datetime.now()

while app_is_running: 
    
    try:
        active_window = pywin.GetWindowText(pywin.GetForegroundWindow())
        current_time = datetime.now()
        time_active = {
            "starting_time": starting_time,
            "current_time": current_time,
            "time_spent": current_time - starting_time,
        }
         
        print(
            f"Active window: {active_window}, "
            f"Started: {time_active['starting_time']}, "
            f"Current: {time_active['current_time']}, "
            f"Time active: {time_active['time_spent']}"
        )

    except Exception as e:
        print(e)

def check_running_apps():
    #get all the running processes
    return apps

def check_active_window():
    #get the active window
    return active_window

def applogs():
    #log the active window and time spent
    return applogs
