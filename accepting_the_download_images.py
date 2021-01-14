import pyautogui

def accept(way_to_image):
    f = open('coordinates.txt')
    mass = []
    for line in f.readlines():
        mass.append(int(line))
    way_to_image.encode('utf-8')
    pyautogui.click(mass[0],mass[1])
    pyautogui.typewrite(way_to_image)
    pyautogui.click(mass[2],mass[3])
