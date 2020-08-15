import functions
from time import sleep as sleep
import pyautogui
import regions


# user input's

stage = input("Input level as World-stage, 1-1 up to 10-4: ")
reruns = input("Input how many reruns : ")


# map selector

functions.find_img("weigh_anchor.png")
sleep(1)
if not functions.find_img_no_click("worlds/world_" + stage[0] + ".png"):
    print("nie znalazło świata")
    for x in range(13):
        pyautogui.click(int(regions.previous_stage[0]), int(regions.previous_stage[1]))
    while not functions.find_img_no_click("worlds/world_" + stage[0] + ".png"):
        pyautogui.click(int(regions.next_stage[0]), int(regions.next_stage[1]))

for x in range(int(reruns)):
    sleep(1.25)
    functions.find_img("stages/stage_" + stage + ".png")
    sleep(2)
    pyautogui.click(regions.random_start_combat)
    sleep(.2)
    pyautogui.click(regions.random_confirm_combat)
    sleep(4)

# combat brain(let)
    functions.find_enemy_engage_combat()
