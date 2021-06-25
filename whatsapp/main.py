import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep

import random
sleep(3)

position1 = pt.locateOnScreen("C:/Users/HP/PycharmProjects/tensorflow/whatsapp_aytoreply/whatsapp/smily_paper.png", confidence=0.5)
x = position1[0]
y = position1[1]


#getting message

def get_message():
    global x,y

    position = pt.locateOnScreen("C:/Users/HP/PycharmProjects/tensorflow/whatsapp_aytoreply/whatsapp/smily_paper.png", confidence= 0.5)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration =.5)
    pt.moveTo(x+90, y-40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message recieved: "+ whatsapp_message)
    return whatsapp_message


    # Copies the message that we want to process
def get_message(self):
    mouse.click(Button.left, 3)
    sleep(self.speed)
    mouse.click(Button.right, 1)
    sleep(self.speed)
    pt.moveRel(10, 10, duration=self.speed)  # x,y has to be adjusted depending on your computer
    mouse.click(Button.left, 1)
    sleep(1)

    # Gets and processes the message
    self.message = pc.paste()
    print('User says: ', self.message)


#post message
def post_responce(message):
    global x, y

    position = pt.locateOnScreen("C:/Users/HP/PycharmProjects/tensorflow/whatsapp_aytoreply/whatsapp/smily_paper.png",
                                 confidence=0.5)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200, y+20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    #pt.typewrite("\n", interval=.01)

post_responce(get_message())