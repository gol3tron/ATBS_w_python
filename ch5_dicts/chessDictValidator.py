#import stuffs


#def function
def isValidChessBoard(board):
    #takes chess board dict input and returns true/false if the board is valid
    #valid board has 1 king of each color
    valid = True

    if ('bking' and 'wking') not in board.values():
        print("missing black or white king")
        valid = False

    kingCountW = 0
    kingCountB = 0

    for val in board.values():
        if val == 'bking':
            kingCountB += 1
        elif val == 'wking':
            kingCountW += 1

    if (kingCountB or kingCountW) > 1:
        print("too many kings!")
        valid = False

    #each player has max 16 pcs
    wcount = 0
    bcount = 0
    #piece names begin with 'w' or 'b' and 'pawn', 'knight', 'bishop' etc
    validPieces = ['wpawn','wrook','wknight','wbishop','wqueen','wking','bpawn','brook','bknight','bbishop','bqueen','bking']

    for val in board.values():
        if val not in validPieces:
            print("possible bad input found: "+val)
            valid = False
        else:
            if val[0] == 'w':
                #the piece is white
                wcount += 1
            elif val[0] == 'b':
                #the piece is black
                bcount += 1


    if (wcount or bcount) > 16:
        print("white or black has > 16 pcs")
        valid = False

    #max 8 pawns
    numPawnsW = 0
    numPawnsB = 0

    for val in board.values():
        if val == 'wpawn':
            numPawnsW += 1
        elif val == 'bpawn':
            numPawnsB += 1

    if (numPawnsB or numPawnsW) > 8:
        print("white or black has > 8 pawns")
        valid = False

    #all pcs must be on valid space from 1a to 8h
    for key in board.keys():
        if len(key) > 2:
            print("invalid key length: "+key)
            valid = False
        elif int(key[0]) > 8:
            print("invalid key: "+key)
            valid = False
        elif key[1] > 'h':
            print("invalid key: "+key)
            valid = False

    if valid:
        return True
    else:
        return False

#main program
if __name__ == '__main__':
    chess0 = {'1h':'bking','6c':'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking'}
    chess1 = {'1h':'bking','6c':'bking','2g':'bbishop','5h':'bqueen','3e':'wking'}
    chess2 = {'1h':'bking','6c':'bbishop','2g':'bbishop','5h':'bbishop','3e':'wking'}
    chess3 = {'1h':'bking','6c':'bbishop','2g':'bbishop','5h':'bbishop','9z':'wking'}
    chess4 = {'1h':'bking','6c':'bbishop','2g':'bbishop','5h':'bbishop','9z':'hellooooo'}

    #print(isValidChessBoard(chess0))
    #print(isValidChessBoard(chess1))
    #print(isValidChessBoard(chess2))
    #print(isValidChessBoard(chess3))
    print(isValidChessBoard(chess4))
