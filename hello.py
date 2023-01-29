import random

import pyautogui as pg

import time

custom_msg = ('Ridhima','Ridhima')

time.sleep(5)

fixed_msg = " Welcome back to thapar "
for i in range(10):
    a = random.choice(custom_msg)
    pg.write(fixed_msg + a)
    pg.press('enter')