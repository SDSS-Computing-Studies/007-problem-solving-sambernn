#game: https://www.clickerheroes.com/play.html

import time as t
import pyautogui as p

def clicker():
    #locate monster and click
    myList = p.locateCenterOnScreen("shop.png", grayscale=True, confidence=0.8)
    print(myList)
    p.moveTo(myList[0],myList[1] - 200)
    p.click(clicks=30, interval = 0.1)
    
def upgrade():
    #purchase upgrades once apropriate amount of gold is made
    pass

def switch():
    #switch stage after beating monster a certain number of times
    pass

def fail():
    #go back a stage if cannot beat boss
    pass

def main():
    clicker()
    pass

clicker()

