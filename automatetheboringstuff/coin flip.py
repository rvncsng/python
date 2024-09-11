# COIN FLIP
import random
numberOfStreaks = 0

def createList():
    coinList = []
    for i in range(100):
        coinList.append(random.randint(0,1))

    return coinList

def countStreak(coinList):
    streak = 0
    count = 0
    for i in range(len(coinList) - 6):
        side = coinList[i]
        if streak == 1:
            break

        for j in range(i, i + 6):
            if count == 6:
                streak=1
                break

            if side == coinList[j]:
                count += 1
                continue
            else:
                count = 0
                break

    return streak

for experimentNumber in range(1000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinList = createList()

    numberOfStreaks += countStreak(coinList)

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
