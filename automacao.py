import pyautogui, sys
import pyperclip
import time
import os

pyautogui.click(x=460,y=750,clicks=1)
time.sleep(2)
pyautogui.hotkey("ctrl","t")
time.sleep(2)
pyperclip.copy("drive.google.com")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

#ver a posição do mouse em tempo real
#! python3
# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')