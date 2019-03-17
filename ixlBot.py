# Output Code For IXL D.1 First Grade Level
# Make Sure To Have The Ixl Tab, Glitch Editor Tab, Then The Glitch Output Tab. (In The That Order)
# Also Make Sure That The Glitch Editor document.write Is Blank
import time

import pyautogui

pyautogui.FAILSAFE = True

# Find Submit Button
# submitButtonLocation = pyautogui.locateOnScreen('')

# Screen = 1 is Main Monitior, Screen = 2 is Laptop
# screen = 2
# New Res Recognition System

onlaptop = False
# Laptop Is 1366, 768 Monitior Is 1920, 1080
laptopresX = 1366
laptopresY = 768

monresX = 1920
monresY = 1080

oldResolutionX = laptopresX
oldResolutionY = laptopresY

laptopcoord1 = 215, 334

# Screen Conversion Function, Note To Self, This Is Literal Garbage
def convertToMainMonitior (startingcoordX, startingcoordY):
    if onlaptop == False:
        moncoordX = startingcoordX / laptopresX * monresX
        moncoordY = startingcoordY / laptopresX * monresY
        print(moncoordX, moncoordY)
# Running On Main Monitior
if onlaptop == False:
    print("Running Bot On Main Monitior Settings")

# Running On Laptop
if onlaptop == True:
    print("Running Bot On Laptop Settings")

# Getting The Problem
while True:
    pyautogui.moveTo(convertToMainMonitior(215, 334), duration=0.50)
    time.sleep(1)
    pyautogui.dragTo(290, 355, duration=0.25)
    time.sleep(1)
    # copies Problem
    pyautogui.hotkey('ctrl', 'c')
    # Takes to glitch script tab
    pyautogui.click(360, 19, duration=0.25)
    # Inputs Problem
    pyautogui.click(335, 261, duration=0.25)
    pyautogui.hotkey('ctrl', 'v')
    # ixloutput tab
    pyautogui.click(597, 12, duration=0.25)
    # Copy Answer
    time.sleep(2)
    pyautogui.moveTo(1, 87, duration=0.25)
    pyautogui.dragTo(30, 90, duration=0.25)
    pyautogui.hotkey('ctrl', 'c')
    # Undo Glitch Input
    pyautogui.click(360, 19, duration=0.25)
    pyautogui.hotkey('ctrl', 'z')
    # Goes Back to Ixl Tab
    pyautogui.click(136, 16, duration=0.25)

    # Finds Submit Button
    # submitButtonLocation = pyautogui.locateOnScreen('')
    # pyautogui.click(submitButtonLocation)

    # Tries Horizontal Input  Box
    pyautogui.click(337, 343, duration=0.25)
    pyautogui.hotkey('ctrl', 'v')

    # Tries Vertical Input Box & If Horizontal will submit
    pyautogui.click(230, 407, duration=0.25)
    pyautogui.hotkey('ctrl', 'v')

    # Submits Vertical Input Box
    pyautogui.click(251, 462, duration=0.25)

    # Clicks "Got It" Button In case of Error
    pyautogui.click(946, 440, duration=0.25)

    # Clicks Go Back Button in Case Of Error
    pyautogui.click(641, 464, duration=0.25)
