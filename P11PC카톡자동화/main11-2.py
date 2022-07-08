import pyautogui
import pyperclip
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPostion = pyautogui.locateOnScreen('pic1.png')
print(picPostion)

if picPostion is None:
    picPostion = pyautogui.locateOnScreen('pic2.png')
    print(picPostion)
    
if picPostion is None:
    picPostion = pyautogui.locateOnScreen('pic3.png')
    print(picPostion)
    
clickPostion = pyautogui.center(picPostion)
pyautogui.doubleClick(clickPostion)

pyperclip.copy('이 메세지는 자동으로 보내는 메세지 입니다~~')
pyautogui.hotkey("ctrl", "v")
time.sleep(1.0)

pyautogui.write(['enter'])
time.sleep(1.0)

pyautogui.write(['escape'])
time.sleep(1.0)