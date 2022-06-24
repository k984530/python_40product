import pyautogui
import time
import pyperclip

pyautogui.moveTo(1787, 275,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 860
start_y = 203
end_x = 1896
end_y = 869

pyautogui.screenshot(r'P10오토마우스를활용한자동화\서울날씨.png', region = (start_x, start_y, end_x - start_x, end_y - start_y))