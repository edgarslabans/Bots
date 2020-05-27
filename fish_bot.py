# tutorial of simple fishing bot for mrpg

import time
import pyautogui as pyautogui
from PIL import ImageGrab
import cv2
import numpy as np

#https://ketosgames.itch.io/fishing

average = [0, ]

template = cv2.imread('template.png',0)
w,h = template.shape[::-1]


for r in range(10):
    print("Lets throw the bite! ")

    time.sleep(2)
    pyautogui.moveTo(1100, 300)
    pyautogui.mouseDown()
    time.sleep(0.4)
    pyautogui.mouseUp()
    time.sleep(0.5)

    base_screen = ImageGrab.grab(bbox=(750, 93, 1155, 487))
    base_screen.save(r"C:\Users\Zebiekste\Documents\Python_works\FishingBot\surface.jpg")

    img_rgb = cv2.imread('surface.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.7)
    for pt in zip(*loc[::-1]):
        x = int(pt[0])
        y = int(pt[1])

    last_mean = 0
    current_mean =0
    for i in range(40):
        #try:
        #clean_screen = ImageGrab.grab(bbox=(x, y, x + w, y + h))
        clean_screen = ImageGrab.grab(bbox=(750+x, 93+y, 750+x + w, 93+y + h))
        clean_screen.save(r"C:\Users\Zebiekste\Documents\Python_works\FishingBot\clean.jpg")
        mean = np.mean(clean_screen)
        average.append(mean)


        if last_mean !=0:

            diff = last_mean-mean

            if diff > 1 or diff < -1:
                pyautogui.moveTo(1100, 300)
                print("Catchh")
                pyautogui.mouseDown()
                time.sleep(0.2)
                pyautogui.mouseUp()
                break


        last_mean = mean
        time.sleep(0.1)
        #diff = average[-1] - mean






