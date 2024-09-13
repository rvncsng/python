# Chess Dictionary Validator

def isValidChessBoard(chessBoard):
    #exactly 1 black king, exactly 1 white king
    #at most 16 pieces, at most 8 pawns
    #valid space 1-8 and a-h

    rows = ['1','2','3','4','5','6','7','8']
    columns = ['a','b','c','d','e','f','g','h']
    pieces = ['king', 'queen', 'bishop', 'pawn', 'knight', 'rook']
    colors = ['b', 'w']
    keys = list(chessBoard.keys())
    values = list(chessBoard.values())

    bking = 0
    wking = 0
    pawns = 0

    for key in keys:
        #check if valid space
        if len(key) != 2:
            return False
        else:
            if key[0] not in rows or key[1] not in columns:
                return False

    for value in values:
        #check valid amount of pieces
        if len(values) > 16 or bking > 1 or wking > 1 or pawns > 8:
            return False

        #check if valid piece
        if value[1:] not in pieces:
            return False

        #check if not black or white piece
        if value[0] not in colors:
            return False

        if value == 'bking':
            bking += 1
        elif value == 'wking':
            wking += 1
        elif value[1:] == 'pawn':
            pawns += 1


    return True

chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(chessBoard))
