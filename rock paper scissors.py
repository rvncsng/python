import random as rand
import sys

print('let\'s play ROCK, PAPER, SCISSORS')
print()
moveList = ['r', 'p', 's']
userPick = ''
win = 0
loss = 0
tie = 0

def showScore():
    print(win, 'Wins,', loss, 'Losses,', tie, 'Ties')

def userWin(userMove, opponentMove):
    result = False
    if (userMove == 'r' and opponentMove == 's') or (userMove == 'p' and opponentMove == 'r') or (userMove == 's' and opponentMove == 'p'):
        result = True

    return result

def showResult(win, loss, tie):
    if win == 3:
        return 'congrats! you win'
    elif loss == 3:
        return 'aww, better luck next time!'
    elif tie == 3:
        return 'good mind reader!'

while True:
    showScore()
    result = showResult(win, loss, tie)
    if result != None:
        print(result)
        break

    print('enter your move: r, p, s, or q')
    userMove = input()
    opponentMove = rand.choice(moveList)

    if(userMove == 'q'):
        sys.exit()

    print('Opponent move is', opponentMove, '\n')

    if(userMove == opponentMove):
        tie += 1
    else:
        userWon = userWin(userMove, opponentMove)
        if userWon:
            win += 1
        else:
            loss += 1



