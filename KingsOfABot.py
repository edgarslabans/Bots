# this autogui file is responsible for automated attacking of the nearby monsters in KingsOfAvalon
# The setting up process requires manually entering coordinates of the screen corners
# number of raids should be corrected as well

import time
from random import randrange

import pyautogui as pyautogui
from PIL import ImageGrab
from PIL import Image
import cv2
import numpy as np
import pytesseract
from pytesseract import Output

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.cbook as cbook

import turtle


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pyautogui.FAILSAFE = False

#=============================================================
numberOfAds = 0

x1 = 854
y1 = 147
x2 = 1827
y2 = 689

gameWindW = x2-x1
gameWindH = y2-y1


# the metod searches for image in fragment in the captured screen
# return the centre coordinates of the image fragment (returns 0, 0 if nothing found)
def SearchImgCoord(image):
    output = [0, 0]
    # reading  and processing the image to search for
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]

    #capturing the whole screen
    home_screen = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    home_screen.save(r"C:\Users\Zebiekste\Documents\Python_works\FishingBot\home.PNG")

    home_screen_rgb = cv2.imread('home.PNG')
    home_screen_gray = cv2.cvtColor(home_screen_rgb, cv2.COLOR_BGR2GRAY)


    #searching for the image
    res = cv2.matchTemplate(home_screen_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.7)
    if len(loc[0]) ==0:
        print('Image', image, ' not found')
    else:
        for pt in zip(*loc[::-1]):
            output[0] = int(pt[0])
            output[1] = int(pt[1])

        output[0] = round(output[0]+x1+w/2)
        output[1] = round(output[1] + y1 + h / 2)

        print(image, ' found in screen coordinates',output[0], output[1])

    return output

def CheckAllX(list):
    output = [0, 0]

    for i in list:
        temp = SearchImgCoord(i)
        if temp[0] !=0:
            output = temp
            print(' X identified as', i)
    return output

# the method contains the activities to make one mouse click
# arguments - screen coordinates
def MouseClick(coord1, coord2):
    time.sleep(0.3)
    pyautogui.moveTo(coord1, coord2, 1)
    time.sleep(0.3)
    pyautogui.click()



def drawClickPoint(coord1, coord2):
    #print("Drawing coordinates in : ", coord1, ',', coord2)
    image_file = cbook.get_sample_data(r"C:\Users\Zebiekste\Documents\Python_works\FishingBot\home.PNG")
    img = plt.imread(image_file)
    # Make some example data
    x = coord1
    y = coord2

    # Create a figure. Equal aspect so circles look circular
    fig, ax = plt.subplots(1)
    # ax.set_aspect('equal')

    ax.imshow(img)
    circ = Circle((x, y), 5)
    ax.add_patch(circ)

    # Show the image
    plt.show()


for r in range(0):
    # Run sequence for 1 add click

    numberOfAds = numberOfAds +1
    print("Starting script. Add no #: ", numberOfAds)

    # Checking if watch video option is available
    [xcoord, ycoord]  = SearchImgCoord('WatchVideo.PNG')

    time.sleep(1)
    # click to watch add if true
    if xcoord != 0:
        random1 = randrange(-50, 50, 1)
        random2 = randrange(-50, 50, 1)
        MouseClick(xcoord+random1, ycoord+random2)
    elif xcoord == 0:
        print('something went wrong')
        home_screen = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        home_screen.save(r"C:\Users\Zebiekste\Documents\Python_works\FishingBot\fail.PNG")
        break

    # Trying to locate the X button after the watch time
    randomT = randrange(0, 15, 1)
    time.sleep(40+randomT)
    closeX, closeY = CheckAllX(listOfX)

    if closeX != 0:
        random1 = randrange(-3, 3, 1)
        random2 = randrange(-5, 5, 1)
        drawClickPoint(closeX-x1+random1, closeY-y1+random2)
        MouseClick(closeX+5, closeY)
    else:
        print('Close button not found, clicking in the upper right corner')
        xUpCorner = round(x1 + (x2-x1)*0.97)
        yUpCorner= round(y1 + (y2-y1)*0.019)
        print('xUpCorner, yUpCorner: ', xUpCorner, '', yUpCorner)
        MouseClick(xUpCorner, yUpCorner)
        drawClickPoint(xUpCorner-x1, yUpCorner-y1)

    randomT2 = randrange(0, 5, 1)
    time.sleep(10 + randomT2)


#MouseClick(1639, 94)


def clickHome():
    random = randrange(-30, 30, 1)
    x = x1+round(gameWindW*0.941) + random
    y = y1+round(gameWindH*0.926) + random
    MouseClick(x, y)

def clickSearchIcon():
    random = randrange(-15, 15, 1)

    ratiox = (892-x1)/gameWindW
    ratioy = (593 - y1)/gameWindH
    x = x1+round(gameWindW*0.039) + random
    y = y1+round(gameWindH*0.822) + random
    MouseClick(x, y)

def clickSearchButton():
    random = randrange(-10, 10, 1)
    ratiox = (1020-x1)/gameWindW
    ratioy = (504 - y1)/gameWindH
    x = x1+round(gameWindW*0.17) + random
    y = y1+round(gameWindH*0.658) + random
    MouseClick(x, y)

def clickScreenCentre():
    random = randrange(-15, 15, 1)
    x= x1 +round(gameWindW/2)+random
    y = y1 + round(gameWindH/2) + random
    MouseClick(x, y)

def clickAttack():
    random = randrange(-10, 10, 1)
    ratiox = (1338-x1)/gameWindW
    ratioy = (570 - y1)/gameWindH
    x = x1+round(gameWindW*0.497) + random
    y = y1+round(gameWindH*0.78) + random
    MouseClick(x, y)

def clickMarсh():
    random = randrange(-10, 10, 1)
    ratiox = (1657-x1)/gameWindW
    ratioy = (629 - y1)/gameWindH
    x = x1+round(gameWindW*0.825) + random
    y = y1+round(gameWindH*0.889) + random
    MouseClick(x, y)

def IfMarchInProgress():
    state = False

    x = x1+round(gameWindW*0.2559)
    y = y1+round(gameWindH*0.328)

    snippet = ImageGrab.grab(bbox=(x-3, y-3, x+3, y+3))
    mean = np.mean(snippet)
    #print (mean)
    pyautogui.moveTo(x, y, 1)

    if mean < 50:
        state = True

    return state

def ifSearchIconPresent():
    state = True

    x = x1+round(gameWindW*0.039)
    y = y1+round(gameWindH*0.822)

    snippet = ImageGrab.grab(bbox=(x-5, y-5, x+5, y+5))
    mean = np.mean(snippet)
    #print (mean)
    pyautogui.moveTo(x, y, 1)

    if mean > 90 or mean < 85:
        state = False

    return state



def MonsterFarmingScript():
    numberOfRaids = 0
    for r in range(10):
        # Run sequence for 1 add click
        time.sleep(3)
        numberOfRaids = + 1
        print("Starting march. No #: ", numberOfRaids)
        if ifSearchIconPresent() == False:
            print("Search button could not be found! Breaking the loop")
            break

        clickSearchIcon()
        time.sleep(0 + randrange(0, 2))
        clickSearchButton()
        time.sleep(1 + randrange(0, 2))
        clickScreenCentre()
        time.sleep(0 + randrange(0, 2))
        clickAttack()
        time.sleep(1 + randrange(0, 2))
        clickMarсh()

        tCount = 0
        while IfMarchInProgress():
            time.sleep(10)
            tCount =+10
            print("waiting for march to end")

        print('March ',numberOfRaids,' finished in ',tCount,' seconds' )








#input("Press Enter to continue...")

#time.sleep(3)
#print(pyautogui.position())
#print(IfMarchInProgress())

MonsterFarmingScript()
