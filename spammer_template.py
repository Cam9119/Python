#this is a template for a basic spammer

import pyautogui # this module allows python to emulate keystrokes
import time


file = open('Replace this', 'r') # replace 'Replace this' with a file that has plain text for what you want to spam
# 'r' means that python will read the file

# if I had a file named "sugar" (no suffix), and it just stored lyrics or something, I would put 
# file = open('sugar', 'r')
# REMEMBER: when putting the file name in there, if it's sugar.txt remember to put "sugar.txt" in the open() statement


time.sleep(5) #this gives you time to click on a text box (the program wont do that)
for word in file:
  pyautogui.typewrite(word)
  pyautogui.hotkey('enter')
  # you can also use 'pyautogui.press' or 'pyautogui.keyDown(the key you want it to emulate)' if you use keydown you also need to use 'pyautogui.keyUp(the same key)
  time.sleep(0.3) # this delay is optional
