import pyautogui
import time

time.sleep(1)
print(pyautogui.position())
pyautogui.click(45, 53)

time.sleep(1)
pyautogui.moveTo(1726, 13, 3)
pyautogui.click()

pyautogui.write('visual', interval=0.3)
pyautogui.press('enter')