#!/usr/bin/env python3
import time
import webbrowser
import pyautogui
import os
import subprocess
subprocess.Popen(["putty"])
time.sleep(1)
print("putty opened")
pyautogui.typewrite(['enter'])
time.sleep(2)
pyautogui.typewrite('')
pyautogui.typewrite(['enter'])
time.sleep(1)
pyautogui.typewrite('')
pyautogui.typewrite(['enter'])
time.sleep(1)
os.system('gsettings set org.gnome.system.proxy mode \'manual\'')
webbrowser.open(
    'https://www.google.com/search?q=myip&oq=myip&aqs=chrome..69i57j0l5.3248j0j4&sourceid=chrome&ie=UTF-8')
print('done')
while(1):
    command = input()
    if(command == "exit"):
        os.system('gsettings set org.gnome.system.proxy mode \'none\'')
        os.system('pkill putty')
        break
