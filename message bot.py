import pyautogui
import time
message = 10
while message > 0:
     time.sleep(2)
     pyautogui.typewrite('hey broooooo.')
     pyautogui.press('enter')
     message = message - 1
     

    