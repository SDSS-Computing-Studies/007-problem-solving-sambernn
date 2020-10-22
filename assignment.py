#game: https://www.clickerheroes.com/play.html

import time as t
import pyautogui as p

def clicker():
    #locate monster and click
    myList = p.locateCenterOnScreen("shop.png", grayscale=True, confidence=0.8)
    p.moveTo(myList[0],myList[1] - 200)
    p.click(clicks=10, interval=0.05)

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
    #scrolls to each button in the shop
    p.scroll(-110)
    p.click()

def switch():
    #switch stage after beating monster a certain number of times
    myList = p.locateCenterOnScreen("switch.png", grayscale=True, confidence=0.6)
    p.moveTo(myList[0] - 200,myList[1],duration=0.3)
    p.click()

def fail():
    #go back a stage if cannot beat boss
    pass    

def main():
    #puts all functions together in a main function
    curTime = t.time()
    targets = [curTime + 20, curTime + 10]
    increment = [20,10]

    while True:
        for i in targets:
            if t.time() > i:
                index = targets.index(i)
                targets[index] = t.time() + increment[index]
                print( str(index) + " is up")
                if index == 0:
                    upgrade()
                if index == 1:
                    switch()
        clicker()
    print("time up") 

main()



