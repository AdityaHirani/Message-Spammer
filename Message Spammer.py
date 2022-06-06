import pyautogui as p
import time

a = input("Enter the message you want to send: ")
b = input("Number of messages you want to send: ")
time.sleep(10)
for i in range(int(b)):
    p.typewrite(a)
    p.press('Enter')
