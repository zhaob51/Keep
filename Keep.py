import win32gui
import win32api
import win32con
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

def keep():

    hwnd_title = dict()

    def get_all_hwnd(hwnd,unuse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
            
    win32gui.EnumWindows(get_all_hwnd, 0)

    for h, t in hwnd_title.items():
        if "航天云课堂" in t:
            win32gui.SetForegroundWindow(h)
            win32gui.ShowWindow(h, win32con.SW_MAXIMIZE)
            left = win32gui.GetWindowRect(h)
            win32api.GetCursorPos()
            win32api.SetCursorPos((round((left[0]+left[2])/2), round((left[1]+left[3]) / 2 + 105)))
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            time.sleep(0.5)
            win32gui.ShowWindow(h, win32con.SW_MINIMIZE)

scheduler = BlockingScheduler()
trigger = IntervalTrigger(seconds=240)
scheduler.add_job(keep, trigger)
scheduler.start()