import pyautogui
import os
def getting_coordinates():
    count = 0
    d = open('coordinates.txt')
    for line in d.readlines():
        count += 1
    if count == 4:
        os.system(r'nul>coordinates.txt')
        print('file is empty,\n writing new coordinates')
        f = open('coordinates.txt', 'a')
        f.write(str(pyautogui.position()).split(', ')[0][8:] + '\n')
        f.write(str(pyautogui.position()).split(', ')[1][2:len(str(pyautogui.position()).split(', ')[1]) - 1] + '\n')
        f.close()
        return
    f = open('coordinates.txt', 'a')
    print(pyautogui.position())
    f.write(str(pyautogui.position()).split(', ')[0][8:] + '\n')
    f.write(str(pyautogui.position()).split(', ')[1][2:len(str(pyautogui.position()).split(', ')[1]) -1] + '\n')
    f.close()

