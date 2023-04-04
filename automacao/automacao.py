import pyautogui
import pyperclip
import time
import os
import shutil

hoje = time.localtime()
current_time = time.strftime("%Y%m%d%H%M", hoje)
print(current_time)

newpath = rf"C:/fazer_backup/backup/{current_time}" 
if not os.path.exists(newpath):
    os.makedirs(newpath)

time.sleep(2)

pasta_fonte = "C:/fazer_backup/arquivos_importantes//"
pasta_destino = rf"C:/fazer_backup/backup/{current_time}//" 
for arquivo in os.listdir(pasta_fonte):

    fonte = pasta_fonte + arquivo
    destino = pasta_destino + arquivo
    print("nome do arquivo: " + arquivo)

    if os.path.isfile(fonte):
        shutil.copy(fonte, destino)
        print('copiou:', arquivo)


# # pyautogui.click(x=280,y=1064,clicks=1)
# # time.sleep(10)
# # pyautogui.hotkey("ctrl","t")
# # time.sleep(10)
# # pyperclip.copy("drive.google.com")
# # pyautogui.hotkey("ctrl","v")
# # pyautogui.press("enter")

# pyautogui.hotkey("win", "e")
# time.sleep(5)
# pyautogui.hotkey("ctrl", "l")
# pyperclip.copy("c:/fazer_backup/arquivos_importantes")
# time.sleep(1)
# pyautogui.hotkey("ctrl", "v")
# time.sleep(2)
# pyautogui.press("enter")
# time.sleep(2)
# pyautogui.hotkey("ctrl", "a")
# pyautogui.hotkey("ctrl", "x")
# time.sleep(2)
# pyautogui.hotkey("alt", "up")
# time.sleep(2)
# pyautogui.press("down")
# time.sleep(1)
# pyautogui.press("enter")
# time.sleep(1)
# pyautogui.hotkey("ctrl", "shift", "n")
# time.sleep(1)
# pyautogui.press("esc")
# time.sleep(1)
# pyautogui.press("enter")
# time.sleep(1)
# pyautogui.hotkey("ctrl", "v")
# time.sleep(1)
# pyautogui.hotkey("alt","up")
# time.sleep(1)
# pyautogui.press("f2")
# pyperclip.copy(current_time)
# time.sleep(1)
# pyautogui.hotkey("ctrl", "v")
# time.sleep(1)
# pyautogui.press("enter")
# time.sleep(1)
# pyautogui.hotkey("ctrl", "w")

# # pyautogui.click(x=1350,y=355,clicks=1)
# # pyperclip.copy("C:/backupiada")
# # pyautogui.hotkey("ctrl", "v")
# # time.sleep(2)
# # pyautogui.press("enter")
# # time.sleep(2)
# # pyautogui.click(x=1350 ,y=500,clicks=1)
# # pyautogui.hotkey("ctrl", "a")

# # ver a posição do mouse em tempo real
# # ! python3
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