import pyscreenshot as ImageGrab
import cv2
import numpy as np
import pyautogui
import time
import random


def screen_update():
    # Takes screenshot
    im = ImageGrab.grab(bbox=(0, 0, 1635, 960))
    im.save("assets/screenshot.png")


def weigh_anchor():
    screen_update()
    screenshot = cv2.imread("assets/screenshot.png")
    test_picture = cv2.imread("assets/weigh_anchor.png")
    res = cv2.matchTemplate(screenshot, test_picture, cv2.TM_CCOEFF_NORMED)
    height, width = test_picture.shape[:2]
    value, location = cv2.minMaxLoc(res)[1], cv2.minMaxLoc(res)[3]
    region = (location[0], location[1], width, height)
    threshold = 0.90
    loc = np.where(res >= threshold)
    found_it = list(loc[0])
    randomize_w = random.randint(region[0], region[0] + width)
    randomize_y = random.randint(region[1], region[1] + height)
    if found_it:
        pyautogui.click(x=randomize_w, y=randomize_y)
    else:
        print("Nie znalazło WA")


def select_map():
    screen_update()
    screenshot = cv2.imread("assets/screenshot.png")
    test_picture = cv2.imread("assets/stage1_4.png")
    res = cv2.matchTemplate(screenshot, test_picture, cv2.TM_CCOEFF_NORMED)
    height, width = test_picture.shape[:2]
    value, location = cv2.minMaxLoc(res)[1], cv2.minMaxLoc(res)[3]
    region = (location[0], location[1], width, height)
    threshold = 0.90
    loc = np.where(res >= threshold)
    found_it = list(loc[0])
    randomize_w = random.randint(region[0], region[0] + width)
    randomize_y = random.randint(region[1], region[1] + height)
    if found_it:
        pyautogui.click(x=randomize_w, y=randomize_y)
        time.sleep(.5)
        pyautogui.click(x=1200, y=700)
        time.sleep(.5)
        pyautogui.click(x=1375, y=808)
    else:
        print("didnt find the level")


def combat_fleet1():
    screen_update()
    screenshot = cv2.imread("assets/screenshot.png")
    test_picture = cv2.imread("assets/light_1.png")
    res = cv2.matchTemplate(screenshot, test_picture, cv2.TM_CCOEFF_NORMED)
    height, width = test_picture.shape[:2]
    value, location = cv2.minMaxLoc(res)[1], cv2.minMaxLoc(res)[3]
    region = (location[0], location[1], width, height)
    threshold = 0.85
    loc = np.where(res >= threshold)
    found_it = list(loc[0])
    if not found_it:
        combat_fleet2()
    else:
        randomize_w = random.randint(region[0], region[0] + width)
        randomize_y = random.randint(region[1], region[1] + height)
        if found_it:
            pyautogui.click(x=randomize_w + 50, y=randomize_y + 100)
            time.sleep(5)
            pyautogui.click(x=1470, y=850)
        else:
            print("Nie znalazło mobka")


def combat_fleet2():
    screen_update()
    screenshot = cv2.imread("assets/screenshot.png")
    test_picture = cv2.imread("assets/light_2.png")
    res = cv2.matchTemplate(screenshot, test_picture, cv2.TM_CCOEFF_NORMED)
    height, width = test_picture.shape[:2]
    value, location = cv2.minMaxLoc(res)[1], cv2.minMaxLoc(res)[3]
    region = (location[0], location[1], width, height)
    threshold = 0.85
    loc = np.where(res >= threshold)
    found_it = list(loc[0])
    if not found_it:
        combat_fleet3()
    else:
        randomize_w = random.randint(region[0], region[0] + width)
        randomize_y = random.randint(region[1], region[1] + height)
        if found_it:
            pyautogui.click(x=randomize_w + 50, y=randomize_y + 100)
            time.sleep(5)
            pyautogui.click(x=1470, y=850)
        else:
            print("Nie znalazło mobka")


def combat_fleet3():
    screen_update()
    screenshot = cv2.imread("assets/screenshot.png")
    test_picture = cv2.imread("assets/light_3.png")
    res = cv2.matchTemplate(screenshot, test_picture, cv2.TM_CCOEFF_NORMED)
    height, width = test_picture.shape[:2]
    value, location = cv2.minMaxLoc(res)[1], cv2.minMaxLoc(res)[3]
    region = (location[0], location[1], width, height)
    threshold = 0.85
    loc = np.where(res >= threshold)
    found_it = list(loc[0])
    randomize_w = random.randint(region[0], region[0] + width)
    randomize_y = random.randint(region[1], region[1] + height)
    if found_it:
        pyautogui.click(x=randomize_w + 50, y=randomize_y + 100)
        time.sleep(5)
        pyautogui.click(x=1470, y=850)
    else:
        print("Nie znalazło mobka")


def combat():
    screen_update()
    screenshot = cv2.imread("assets/screenshot.png")
    test_picture = cv2.imread("assets/boss_node.png")
    res = cv2.matchTemplate(screenshot, test_picture, cv2.TM_CCOEFF_NORMED)
    height, width = test_picture.shape[:2]
    value, location = cv2.minMaxLoc(res)[1], cv2.minMaxLoc(res)[3]
    region = (location[0], location[1], width, height)
    threshold = 0.90
    loc = np.where(res >= threshold)
    found_it = list(loc[0])
    if not found_it:
        combat_fleet1()
    else:
        randomize_w = random.randint(region[0], region[0] + width)
        randomize_y = random.randint(region[1], region[1] + height)
        if found_it:
            pyautogui.click(x=randomize_w, y=randomize_y)
            time.sleep(5)
            pyautogui.click(x=1470, y=850)
        else:
            print("Nie znalazło bossa")


