# TIC TAC TOE using dictionaries
theBoard = {'TL': ' ', 'TM': ' ', 'TR': ' ', 'ML': ' ', 'MM':
' ', 'MR': ' ', 'LL': ' ', 'LM': ' ', 'LR': ' '}

def printBoard(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])

def checkBoard(board, turn):

    #horizontal
    if (board['TL'] == board['TM'] == board['TR'] != ' ') or (board['ML'] == board['MM'] == board['MR'] != ' ') or (board['LL'] == board['LM'] == board['LR'] != ' '):
        return 1

    #vertical
    if (board['TL'] == board['ML'] == board['LL'] != ' ') or (board['TM'] == board['MM'] == board['LM'] != ' ') or (board['TR'] == board['MR'] == board['LR'] != ' '):
        return 1

#         diagonal
    if (board['TL'] == board['MM'] == board['LR'] != ' ') or (board['LL'] == board['MM'] == board['TR'] != ' '):
        return 1

    return 0


turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('It is', turn, '\'s turn.', 'Move on which space?')
    move = input()
    theBoard[move] = turn

    result = checkBoard(theBoard, turn)
    if result == 1:
        printBoard(theBoard)
        print(turn, 'is the winner!')
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
