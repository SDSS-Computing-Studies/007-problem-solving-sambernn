#game: https://www.clickerheroes.com/play.html

import time as t
import pyautogui as p

def clicker():
    #locate monster and click
    myList = p.locateCenterOnScreen("shop.png", grayscale=True, confidence=0.8)
    p.moveTo(myList[0],myList[1] - 200)
    while True:
        p.click()

def upgrade():
    #purchase upgrades once apropriate amount of gold is made
    myList = p.locateCenterOnScreen("upgrade.png", grayscale=True, confidence=0.8)
    p.moveTo(myList[0],myList[1] + 130,duration=0.3)
    p.click()
    count = 0
    while count < 30:
        buy()
        count = count + 1
    p.scroll(2000)
        
def buy():
    p.scroll(-110)
    p.click()

def switch():
    #switch stage after beating monster a certain number of times
    myList = p.locateCenterOnScreen("switch.png", grayscale=True, confidence=0.7)
    p.moveTo(myList[0] - 130,myList[1],duration=0.3)
    p.click()

def fail():
    #go back a stage if cannot beat boss
    pass

def main():
    clicker()
    upgrade()

switch()



