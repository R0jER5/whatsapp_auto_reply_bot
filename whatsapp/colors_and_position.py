import pyautogui as pt
from time import sleep

while True:
    posXY= pt.position()#get the position of our mouse pointer
    print(posXY, pt.pixel(posXY[0], posXY[1]))#x position=0, y position =1
    sleep(1)# 1 sec delay
    if posXY[0] == 0:
        break
