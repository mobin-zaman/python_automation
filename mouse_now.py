#! python3
#mouse_now.py - display the mouse cursor's current position

import pyautogui
print('press ctrl-c to quit')

try:
    while True:
        x,y=pyautogui.position()
        position_str='x: '+ str(x).rjust(4)+' y: '+str(y).rjust(4)
        print(position_str,end='')
        print('\b'*len(position_str),end='',flush=True)

except KeyboardInterrupt:
    print('\ndone')