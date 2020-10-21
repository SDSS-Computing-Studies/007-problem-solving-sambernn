#!python3

import time

curTime = time.time()

targetTime = curTime + 30 

targets = [curTime + 5, curTime + 7]

while True:
    for i in targets:
        if time.time() > i:
            index = targets.index(i)
            print( str(i) + " is up")
    click()
print("time up")