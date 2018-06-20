import pyautogui
import time
import subprocess

def animiraniLogo():
    subprocess.call(["xdotool", "windowactivate", "16777221"])
    pyautogui.hotkey('alt', '1')
    time.sleep(14)
    pyautogui.hotkey('alt', '1')

animiraniLogo()