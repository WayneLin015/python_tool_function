import os 
import cv2
import numpy as np
import win32api
import win32gui
import win32con
import subprocess
import pyautogui
from PIL import Image
import time
import random

hwnd = win32gui.FindWindow(None, "BlueStacks") 
left, top, right, bottom = win32gui.GetWindowRect(hwnd)

print(left, top, right, bottom)

win32gui.MoveWindow(hwnd, left, top, 600, 1000, True)

w = right - left # width
h = bottom - top # height

def time_sleep_range(low_bound, up_bound):
    time.sleep(random.uniform(low_bound,up_bound))


def upgrade_spell(left_add, top_add):
    pyautogui.click(left+left_add,top+top_add)
    time_sleep_range(0.5, 1.5)

def click_info():
    pyautogui.click(left+48,top+975)
    time_sleep_range(0.5, 1.5)

def click_player(left_add, top_add):
    pyautogui.click(left+left_add,top+top_add)
    time_sleep_range(0.5, 1.5)

def inital():
    time_sleep_range(2,3)

    click_info()
    click_player(465, 200)

    # click spell and upgrade
    for i in range(6):
        pyautogui.click(left+460,top+430+i*85)
        time.sleep(0.5)
        upgrade_spell(330,430+i*85) 

    click_info()

def prestige():
    time.sleep(random.uniform(3,6))

    pyautogui.click(left+48,top+975)
    time.sleep(random.uniform(0.5,3))

    pyautogui.click(left+460,top+315)
    time.sleep(random.uniform(0.5,3))   

    pyautogui.click(left+275,top+875)
    time.sleep(random.uniform(0.5,3))

    pyautogui.click(left+375,top+725)
    time.sleep(random.uniform(7,8))

def cancel_skill_mid():

    click_info()

    pyautogui.click(left+460,top+515)
    time_sleep_range(0.5,1)   
    
    click_info()

def cancel_skill_last():

    click_info()

    pyautogui.click(left+460,top+515)
    time_sleep_range(0.5,1)

    pyautogui.click(left+460,top+855)
    time_sleep_range(0.5,1)    
    
    click_info()


def click_skill():
    for i in range(5):
        pyautogui.click(left+135+i*90,top+895)
        time.sleep(random.uniform(0.5,1.5))


def auto_click():
    t_end = time.time()+230
    while time.time() < t_end:
        x = random.randrange(175,440)
        y = random.randrange(400,560)
        pyautogui.click(left+x,top+y)
        time_sleep_range(0.1,0.3)
        
def round_play():
    
    click_skill()
    auto_click()
    time_sleep_range(1,1.5)
    cancel_skill_mid()
    time_sleep_range(5,7)

    click_skill()
    auto_click()
    time_sleep_range(1,1.5)
    cancel_skill_last()
    time_sleep_range(5,7)

def sc_play():
    round_play()
    time_sleep_range(2,3)
    round_play()
    time_sleep_range(1,2)



for i in range(2):
    start = time.time()
    inital()
    sc_play()
    prestige()
    stop = time.time()
    print('duration: ', stop-start)



# prestige()


