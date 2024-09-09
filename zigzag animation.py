# ZIGZAG ANIMATION
import time

increment = 0
movement = 0
dots = '********'
space = ' '

def calculateIncrement(increment, movement):
    increment = movement + increment
    return increment

def getMovement(increment, movement):
    if(increment == 5):
        movement = -1
    elif(increment == 0):
        movement = 1

    return movement

while True:
    print(space * increment + dots)
    time.sleep(0.1)
    movement = getMovement(increment, movement)
    increment = calculateIncrement(increment, movement)



