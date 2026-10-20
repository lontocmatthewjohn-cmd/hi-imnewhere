import win32gui
import win32process
import psutil, os
from datetime import datetime

def main():
    app_is_running = False
    starting_time = datetime.now()

    while app_is_running:
        try:
            active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
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

    check_active_window()
def check_running_apps():
    #get all the running processes
    return apps

def check_active_window():
    print("checking Current Window")
    hwnd = win32gui.GetForegroundWindow()
    ActiveThreadProcessId = win32process.GetWindowThreadProcessId(hwnd)
    p = psutil.Process(ActiveThreadProcessId[1])
    print(p.name())
    return win32gui.GetWindowText(hwnd)

def applogs():
    #log the active window and time spent
    return applogs


if __name__ == "__main__":
    main()
