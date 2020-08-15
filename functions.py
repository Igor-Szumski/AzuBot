import pyscreenshot as ImageGrab
import cv2
import numpy as np
import pyautogui
import time
import random


def screen_update():
    im = ImageGrab.grab(bbox=(0, 0, 1635, 960))
    im.save("assets/screenshot.png")


def find_img(img):
    screen_update()
    screenshot = cv2.imread("assets/screenshot.png")
    test_picture = cv2.imread("assets/" + img)
    res = cv2.matchTemplate(screenshot, test_picture, cv2.TM_CCOEFF_NORMED)
    height, width = test_picture.shape[:2]
    value, location = cv2.minMaxLoc(res)[1], cv2.minMaxLoc(res)[3]
    region = (location[0], location[1], width, height)
    threshold = 0.90
    loc = np.where(res >= threshold)
    found_it = list(loc[0])
    randomize_w = random.randint(region[0]+2, region[0] + width-4)
    randomize_y = random.randint(region[1]+2, region[1] + height-4)
    if found_it:
        pyautogui.click(x=randomize_w, y=randomize_y)
        return True
    else:
        print("Nie znalazło : " + img)
        return False


def find_img_no_click(img):
    screen_update()
    screenshot = cv2.imread("assets/screenshot.png")
    test_picture = cv2.imread("assets/" + img)
    res = cv2.matchTemplate(screenshot, test_picture, cv2.TM_CCOEFF_NORMED)
    threshold = 0.90
    loc = np.where(res >= threshold)
    found_it = list(loc[0])
    if found_it:
        print("(n)Znalazło : " + img)
        return True
    else:
        print("(n)Nie znalazło : " + img)
        return False


def find_img_enemy(img, update):
    if update == 1:
        screen_update()
    screenshot = cv2.imread("assets/screenshot.png")
    test_picture = cv2.imread("assets/" + img)
    res = cv2.matchTemplate(screenshot, test_picture, cv2.TM_CCOEFF_NORMED)
    height, width = test_picture.shape[:2]
    value, location = cv2.minMaxLoc(res)[1], cv2.minMaxLoc(res)[3]
    region = (location[0], location[1], width, height)
    threshold = 0.88
    loc = np.where(res >= threshold)
    found_it = list(loc[0])
    if img == "boss_node.png":
        randomize_w = random.randint(region[0], region[0] + width)
        randomize_y = random.randint(region[1], region[1] + height)
    else:
        randomize_w = random.randint(region[0] + 16, region[0] + 126)
        randomize_y = random.randint(region[1] + 34, region[1] + 144)
    if found_it:
        pyautogui.click(x=randomize_w, y=randomize_y)
        print("znalazło : " + img)
        return True
    else:
        print("Nie znalazło : " + img)
        return False


def find_enemy_engage_combat():
    time.sleep(4)
    emergency_search = 0
    while not find_img_enemy("boss_node.png", 1):
        if find_img_enemy("light_1.png", 0):
            time.sleep(.7)
            if find_img_no_click("3-4fixit.png"):
                time.sleep(.4)
                find_img_enemy("light_2.png", 0)
                time.sleep(.7)
                if find_img_no_click("3-4fixit.png"):
                    time.sleep(.4)
                    find_img_enemy("light_3.png", 0)
                    start_combat_and_evade_ambush()
                else:
                    start_combat_and_evade_ambush()
            start_combat_and_evade_ambush()

        elif find_img_enemy("light_2.png", 0):
            time.sleep(.7)
            if find_img_no_click("3-4fixit.png"):
                time.sleep(.4)
                find_img_enemy("light_1.png", 0)
                time.sleep(.7)
                if find_img_no_click("3-4fixit.png"):
                    time.sleep(.4)
                    find_img_enemy("light_3.png", 0)
                    start_combat_and_evade_ambush()
                else:
                    start_combat_and_evade_ambush()
            start_combat_and_evade_ambush()

        elif find_img_enemy("light_3.png", 0):
            time.sleep(.7)
            if find_img_no_click("3-4fixit.png"):
                time.sleep(.4)
                find_img_enemy("light_1.png", 0)
                time.sleep(.7)
                if find_img_no_click("3-4fixit.png"):
                    time.sleep(.4)
                    find_img_enemy("light_2.png", 0)
                    start_combat_and_evade_ambush()
                else:
                    start_combat_and_evade_ambush()
            start_combat_and_evade_ambush()

        else:
            print("Didn't find any enemies")
            emergency_search = emergency_search + 1
            time.sleep(3)
        if emergency_search == 2:
            print("Resulting to emergency search: ")
            find_img_enemy("emergency/highest/3-4_enemy_bottom_1.png", 0)
            find_img_enemy("emergency/highest/3-4_enemy_bottom+1_1.png", 0)
            find_img_enemy("emergency/highest/3-4_enemy_bottom_line_2.png", 0)
            find_img_enemy("emergency/highest/3-4_enemy_middle_line_2.png", 0)
            find_img_enemy("emergency/highest/3-4_enemy_top_2.png", 0)
    start_combat_and_evade_ambush()


def finish_combat():
    if find_img_no_click("touch_to_continue.png"):
        time.sleep(.5)
        find_img("touch_to_continue.png")
        time.sleep(.2)
        find_img("touch_to_continue_after.png")
        time.sleep(1.22)
        find_img("finish.png")
        time.sleep(4)
        find_img("fixit.png")
        time.sleep(4)
    else:
        time.sleep(3)
        finish_combat()


def start_combat_and_evade_ambush():
    fail = 0
    success = 0
    while success == 0 and fail <= 5:
        time.sleep(.5)
        if find_img_no_click("start_combat.png"):
            time.sleep(.5)
            find_img("start_combat.png")
            success = success + 1
        elif find_img_no_click("flee.png"):
            time.sleep(.5)
            find_img("flee.png")
            time.sleep(2)
            if find_img_no_click("start_combat.png"):
                time.sleep(.5)
                find_img("start_combat.png")
                success = success + 1
        else:
            fail = fail + 1
            print("fail " + str(fail))
            time.sleep(.5)
    print("success " + str(success))
    if success > 0:
        time.sleep(30)
        finish_combat()
    else:
        find_enemy_engage_combat()

