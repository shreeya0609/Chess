import pygame
import random
import copy

pygame.init()
screen = pygame.display.set_mode([700,700 ])

class piece():
    def __init__(self, xpos, ypos, name, color, typ):
        self.xpos = xpos
        self.ypos = ypos
        self.name = name
        self.color = color
        self.typ = typ
        self.first = True
        self.enp = 0


chessBoard = [
    [None, None, None, None, None, None, None, None],[None, None, None, None, None, None, None, None],[None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],[None, None, None, None, None, None, None, None],[None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],[None, None, None, None, None, None, None, None]]


black = [piece(0, 0, "bR", "Black", "Rook"),piece(0, 1, "bN", "Black", "Knight"),piece(0, 2, "bB", "Black", "Bishop"),piece(0, 3, "bQ", "Black", "Queen"),
    piece(0, 4, "bK", "Black", "King"),piece(0, 5, "bB", "Black", "Bishop"),piece(0, 6, "bN", "Black", "Knight"),piece(0, 7, "bR", "Black", "Rook"),
    piece(1, 0, "bP", "Black", "Pawn"),piece(1, 1, "bP", "Black", "Pawn"),piece(1, 2, "bP", "Black", "Pawn"),piece(1, 3, "bP", "Black", "Pawn"),
    piece(1, 4, "bP", "Black", "Pawn"),piece(1, 5, "bP", "Black", "Pawn"),piece(1, 6, "bP", "Black", "Pawn"),piece(1, 7, "bP", "Black", "Pawn")]


white = [
    piece(7, 0, "wR", "White", "Rook"),piece(7, 1, "wN", "White", "Knight"),piece(7, 2, "wB", "White", "Bishop"),piece(7, 3, "wQ", "White", "Queen"),
    piece(7, 4, "wK", "White", "King"),piece(7, 5, "wB", "White", "Bishop"),piece(7, 6, "wN", "White", "Knight"),piece(7, 7, "wR", "White", "Rook"),
    piece(6, 0, "wP", "White", "Pawn"),piece(6, 1, "wP", "White", "Pawn"),piece(6, 2, "wP", "White", "Pawn"),piece(6, 3, "wP", "White", "Pawn"),
    piece(6, 4, "wP", "White", "Pawn"),piece(6, 5, "wP", "White", "Pawn"),piece(6, 6, "wP", "White", "Pawn"),piece(6, 7, "wP", "White", "Pawn")]


for piece in black:
    chessBoard[piece.xpos][piece.ypos] = piece
for piece in white:
    chessBoard[piece.xpos][piece.ypos] = piece


def pawn(piece, board):
    possible = []
    dir = []
    if piece.color == "Black":
        x = piece.xpos
        y = piece.ypos
        if piece.first == True:
            if (0 <= x+2 <= 7) and (0 <= y <= 7):
                if board[x+1][y] == None and board[x+2][y] == None:
                    possible.append( (0, piece.xpos, piece.ypos, x+2, y) )
        if (0 <= x+1 <= 7) and (0 <= y <= 7):
            if board[x+1][y] == None:
                possible.append( (0, piece.xpos, piece.ypos, x+1, y) )
        dir = [ (1, -1), (1, 1) ]
    else:
        x = piece.xpos
        y = piece.ypos
        if piece.first == True:
            if (0 <= x-2 <= 7) and (0 <= y <= 7):
                if board[x-1][y] == None and board[x-2][y] == None:
                    possible.append( (0, piece.xpos, piece.ypos, x-2, y) )
        
        if (0 <= x-1 <= 7) and (0 <= y <= 7):
            if board[x-1][y] == None:
                possible.append( (0, piece.xpos, piece.ypos, x-1, y) )
        dir= [(-1, -1), (-1, 1), ]

    
    for p in dir:
        x = piece.xpos+p[0]
        y = piece.ypos+p[1]
        if ( (0 <= x <= 7) and (0 <= y <= 7) ):
            if (board[x][y]!=None):
                if board[ x ][ y ].color != piece.color:  
                    possible.append( (1, piece.xpos, piece.ypos, x, y) )
    return possible


def queen(piece, board):
    opp = "White"
    if piece.color == "White":
        opp = "Black"
    possible = []
    
    dir = [ (-1, 0),(1, 0),(0, 1),(0, -1), (-1, -1),(-1, 1),(1, -1),(1, 1) ] 
    for p in dir:
        x = piece.xpos
        y = piece.ypos
        while( (0 <= (x+p[0]) <= 7) and (0 <= (y+p[1]) <= 7) ):
            x = x+p[0]
            y = y+p[1]
            if board[x][y] == None:
                possible.append( (0, piece.xpos, piece.ypos, x, y) )
            else:
                if board[x][y].color == opp:
                    possible.append( (1, piece.xpos, piece.ypos, x, y) )
                break
    return possible

def rook(piece, board):
    opp = "White"
    if piece.color == "White":
        opp="Black"
    possible = []
    dir = [(-1,0),(1,0),(0,1),(0,-1)]
    for p in dir:
        x = piece.xpos
        y = piece.ypos

        while( (0 <= (x+p[0]) <= 7) and (0 <= (y+p[1]) <= 7) ):
            x = x+p[0]
            y = y+p[1]
            if board[ x ][ y ] == None:
                possible.append((0, piece.xpos, piece.ypos, x, y))
            else:
                if board[x][y].color == opp:
                    possible.append((1, piece.xpos, piece.ypos,x, y))
                break
    return possible
def bishop(piece, board):
    opp="White"
    if piece.color == "White":
        opp = "Black"
    possible=[]
    dir=[(-1,-1),(-1, 1),(1, -1),(1, 1)]
    for p in dir:
        x = piece.xpos
        y = piece.ypos
        while( (0 <= (x+p[0]) <= 7) and (0 <= (y+p[1]) <= 7) ):
            x = x+p[0]
            y = y+p[1]
            if board[ x ][ y ] == None:
                possible.append( (0, piece.xpos, piece.ypos, x, y) )
            else:
                if board[x][y].color == opp:
                    possible.append((1, piece.xpos, piece.ypos,x,y))
                break
    return possible
def knight(piece, board):
    opp="White"
    if piece.color=="White":
        opp="Black"
    possible=[]
    dir=[(-2,-1),(-1,-2),(-2,1),(-1,2),(1,-2),(2,-1),(1,2),(2,1)]
    for p in dir:
        x = piece.xpos+p[0]
        y = piece.ypos+p[1]
        if (0 <= x <= 7) and (0 <= y <= 7):
            if board[ x ][ y ] == None:
                possible.append( (0, piece.xpos, piece.ypos, x, y) )
            else:
                if board[x][y].color == opp:
                    possible.append((1, piece.xpos, piece.ypos,x,y))
    return possible
def getKing(piece, board):
    possible=[]
    dir=[(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    for p in dir:
        x=piece.xpos+p[0]
        y=piece.ypos+p[1]
        if((0<=x<= 7)and (0<=y<=7)):
            if board[x][y] == None:
                possible.append((0,piece.xpos,piece.ypos,x,y))
            else:
                if board[x][y].color!=piece.color:    
                    possible.append((1,piece.xpos,piece.ypos,x,y))
    return possible
def check(king, board):
    if king.color == "White":
        moves = all("Black", board)
    else:
        moves = all("White", board)
    attacking = 0
    for move in moves:
        if move[3] == king.xpos and move[4] == king.ypos:
            attacking += 1
    return attacking > 0

def movepiece(board, moveType, oldX, oldY, newX, newY):
    if moveType == 0 or moveType == 1:
        board[newX][newY] = board[oldX][oldY]
        board[newX][newY].xpos = newX
        board[newX][newY].ypos = newY
        board[newX][newY].first = False
        if board[newX][newY].typ == "Pawn":
            if newX == 0 or newX == 7:
                if board[newX][newY].color == "White" and newX == 0:
                    board[newX][newY].name = "wQ"
                    board[newX][newY].typ = "Queen"
                elif board[newX][newY].color == "Black" and newX == 7:
                    board[newX][newY].name = "bQ"
                    board[newX][newY].typ = "Queen"
        board[oldX][oldY] = None
    
def all(color, board):
    possible = []
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] != None:
                if board[i][j].color == color:
                    if board[i][j].typ == "Queen":
                        possible.extend( queen(board[i][j], board) )
                    elif board[i][j].typ == "Rook":
                        possible.extend( rook(board[i][j], board) )
                    elif board[i][j].typ == "Bishop": 
                        possible.extend( bishop(board[i][j], board) )
                    elif board[i][j].typ == "Knight":
                        possible.extend( knight(board[i][j], board) )
                    elif board[i][j].typ == "Pawn": 
                        possible.extend(pawn(board[i][j], board))
                    elif board[i][j].typ == "King": 
                        possible.extend( getKing(board[i][j], board) )
    return possible

def all2(color, board):
    possible = all(color, board)
    # find king
    king = None
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] != None:
                if board[i][j].typ== "King" and board[i][j].color == color:
                    king = board[i][j]
                    break
    moves2 = []
    for move in possible:
        if board[move[3]][move[4]] == None:
            tmpBoard = copy.deepcopy( board )
            movepiece( tmpBoard, move[0], move[1], move[2], move[3], move[4] )
            if check( king, tmpBoard ) == False:
                moves2.append( move )
        else:
            if board[ move[3] ][ move[4] ].typ != "King":
                tmpBoard = copy.deepcopy( board )
                movepiece( tmpBoard, move[0], move[1], move[2], move[3], move[4] )
                if check( king, tmpBoard ) == False:
                    moves2.append( move )
    possible=moves2
    return possible

def get(color, board):
    king = ""
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] != None:
                if board[i][j].typ == "King" and board[i][j].color == color:
                    king = board[i][j]
                    break

    state = 0
    moves = []
    if king != "":
        if check( king, board):
            state = 1
            moves = getKing( king, board )
            king_moves = []#priority to get king out of check
            for move in moves:
                if board[move[3]][move[4]] != None:
                    if board[move[3]][move[4]].typ == "King":
                        continue
                tmpBoard = copy.deepcopy( board )
                movepiece( tmpBoard, move[0], move[1], move[2], move[3], move[4] )
                if check( tmpBoard[ move[3] ][ move[4] ], tmpBoard ) == False:
                    king_moves.append( move )
            if len( king_moves ) == 0:
                moves = all2(color, board, 0)
                if len(moves) == 0:
                    state = 2
            else:
                moves = king_moves
        else:
            moves = all2(color, board)
            if len(moves) == 0:
                state = 3
    return (state, moves)

def fitness(turn, board):#evaluation function
    whitept = 0
    blackpt = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] != None:
                if board[i][j].typ == "Queen":
                    if board[i][j].color == "White":
                        whitept+= 90
                    else:
                        blackpt += 90
                elif board[i][j].typ == "Rook":
                    if board[i][j].color == "White":
                        whitept += 50
                    else:
                        blackpt += 50
                elif board[i][j].typ == "Bishop":
                    if board[i][j].color == "White":
                        whitept += 30
                    else:
                        blackpt += 30
                    
                elif board[i][j].typ == "Knight":
                    if board[i][j].color == "White":
                        whitept += 30
                    else:
                        blackpt += 30
                
                elif board[i][j].typ == "Pawn":
                    if board[i][j].color == "White":
                        whitept += 10
                    else:
                        blackpt += 10
                    
                elif board[i][j].typ == "King":
                    if board[i][j].color == "White":
                        whitept += 900
                    else:
                        blackpt += 900
    return blackpt - whitept
def max_value(turn, board, depth, max_depth):
    if depth == max_depth:
        return ( fitness(turn, board), 0)
    else:
        state, moves = get(turn, board)
        if state== 2 or state == 3 or len(moves) == 0:
            return (-1000, 0)
        else:
            tmpB = copy.deepcopy( board )
            movepiece( tmpB, moves[0][0], moves[0][1], moves[0][2], moves[0][3], moves[0][4] )
            max_ft = fitness(turn, tmpB)
            m_ = moves[0]
            ft_arr = []
            for m in moves:
                tmpBoard = copy.deepcopy( board )
                movepiece(tmpBoard, m[0], m[1], m[2], m[3], m[4])
                f, mv = min_value("White", tmpBoard, depth+1, max_depth)
                if f > max_ft:
                    max_ft = f
                    m_ = mv
                ft_arr.append(f)
            same_moves = [ moves[i] for i in range(0, len(moves)) if ft_arr[i] == f ]
            m_ = random.choice(same_moves)
            return (max_ft, m_)

def min_value(turn, board, depth, max_depth):
    if depth == max_depth:
        return ( fitness(turn, board), 0)
    else:
        state, moves = get(turn, board)
        if state== 2 or state== 3 or len(moves) == 0:
            return (-1000, 0)
        else:
            tmpB = copy.deepcopy( board )
            movepiece( tmpB, moves[0][0], moves[0][1], moves[0][2], moves[0][3], moves[0][4] )
            min_ft = fitness(turn, tmpB)
            m = moves[0]
            ft_arr = []
            for n in moves:
                tmpBoard = copy.deepcopy( board )
                movepiece(tmpBoard, n[0], n[1], n[2], n[3], n[4])
                f, mv = max_value("Black", tmpBoard, depth+1, max_depth)
                if f < min_ft:
                    min_ft = f
                    m = mv
                ft_arr.append(f)
            same_moves = [ moves[i] for i in range(0, len(moves)) if ft_arr[i] == f ]
            m = random.choice(same_moves)
            return (min_ft, m)
def minimax(turn, board):
    if turn == "Black":#maximize
        ft, move_ = max_value("Black", board, 0, 2)
    else:#minimize
        ft, move_ = min_value("White", board, 0, 2)
    return (ft, move_)



state1 = 0 # current overall statuswhite
state2 = 0 # current overall status black
turn = "White"
def show(board):
    for x in range(0, 8):
        for y in range(0, 8):
            if board[x][y] == None:
                print( f"{'*':<3}", end=" ")
            else:
                print( f"{board[x][y].name:<3}", end=" ")
        print("")
    print("\n    ", end="")
    for x in range(0, 8):
        print(f"{chr(97+x):<3}", end=" ")
    print("")


def drawBox(x, y, color, surf):
    color = (255,255,255)
    pygame.draw.rect(surf, color, pygame.Rect(x, y, 60, 60))


Rook_Img = [
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/bR.png'), (60, 60)),
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/wR.png'), (60, 60)),
    ]

Knight_Img = [
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/bN.png'), (60, 60)),
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/wN.png'), (60, 60)),
    ]

Bishop_Img = [
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/bB.png'), (60, 60)),
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/wB.png'), (60, 60)),
    ]

Queen_Img = [
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/bQ.png'), (60, 60)),
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/wQ.png'), (60, 60)),
    ]

King_Img = [
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/bK.png'), (60, 60)),
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/wK.png'), (60, 60)),
    ]

Pawn_Img = [
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/bp.png'), (55, 55)),
    pygame.transform.scale( pygame.image.load('19BEE0182_CHESSPROJECT/images/wp.png'), (55, 55)),
    ]


def Img(surf, img, x, y):
    surf.blit(img, (x+3, y+3) )

def showPieces(surf, board):
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] != None:
                if board[i][j].typ == "Rook":
                    if board[i][j].color == "Black":
                        Img(surf, Rook_Img[0], j*65, i*65 )
                    else:
                        Img(surf, Rook_Img[1], j*65, i*65 )

                if board[i][j].typ == "Knight":
                    if board[i][j].color == "Black":
                        Img(surf, Knight_Img[0], j*65, i*65 )
                    else:
                        Img(surf, Knight_Img[1], j*65, i*65 )

                if board[i][j].typ == "Bishop":
                    if board[i][j].color == "Black":
                        Img(surf, Bishop_Img[0], j*65, i*65 )
                    else:
                        Img(surf, Bishop_Img[1], j*65, i*65 )

                if board[i][j].typ == "Queen":
                    if board[i][j].color == "Black":
                        Img(surf, Queen_Img[0], j*65, i*65 )
                    else:
                        Img(surf, Queen_Img[1], j*65, i*65 )

                if board[i][j].typ == "King":
                    if board[i][j].color == "Black":
                        Img(surf, King_Img[0], j*65, i*65 )
                    else:
                        Img(surf, King_Img[1], j*65, i*65 )

                if board[i][j].typ == "Pawn":
                    if board[i][j].color == "Black":
                        Img(surf, Pawn_Img[0], j*65, i*65 )
                    else:
                        Img(surf, Pawn_Img[1], j*65, i*65 )

def moveToStr(x1, y1, x2, y2):
    return (str(chr(97+y1))+""+str(8-x1) )+" - " +(str(chr(97+y2))+""+str(8-x2) )

def onlykings(board):
    whitePoints = 0
    blackPoints = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] != None:
                if board[i][j].color == "White":
                    whitePoints += 1
                else:
                    blackPoints += 1
    return (blackPoints == 1 and whitePoints == 1)

fc = None  
sc = None   # second move
one_time_white = True
one_time_black = True
moves = []
moves_list = []
status = ""
status_display = False

running = True
while running:
    checkbox = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == "White":
                x,y = pygame.mouse.get_pos()
                x //= 65
                y //= 65
                if fc == None:
                    fc = (x,y)
                elif sc == None:
                    sc = (x, y)
                elif fc != None and sc!= None:
                    fc = (x, y)
                    sc = None
    for x in range(0, 8):
        for y in range(0, 8):
            if checkbox:
                drawBox(x*65, y*65, (214, 214, 214), screen)
            else:
                drawBox(x*65, y*65, (6, 71, 54), screen)
            checkbox = 1 - checkbox
        checkbox = 1 - checkbox
    showPieces(screen, chessBoard)
    pygame.display.flip()

    if onlykings(chessBoard) == True:
        status = "Draw"
        running = False
        continue
    if turn == "Black":
        if one_time_black == True:
            state2, moves = get(turn, chessBoard)
            if state2 == 2:
                status = "Checkmate"
                running =False
            elif state2 == 3:
                status = "Stalemate"
                running = False
            if running == True:
                f, m = minimax("Black", chessBoard)
                movepiece(chessBoard, m[0], m[1], m[2], m[3], m[4])
                moves_list.insert( 0, "B "+chessBoard[m[3]][m[4]].typ+" "+moveToStr(m[1], m[2], m[3], m[4]) )
                
                pygame.time.delay(100)
                
                turn = "White"
                one_time_white == True

    else:
        if one_time_white == True:
            state1, moves = get(turn, chessBoard)
            if state1 == 2:
                status = "Checkmate"
                running = False
            elif state1 == 3:
                status = "Stalemate"
                running = False
            one_time_white = False
        if state1 == 0 or state1 == 1:
            if state1 == 1:
                status = "Checked"
            else:
                status = ""
            if fc != None and sc != None:
                pygame.time.delay(20)
                oldx = fc[1]
                oldy = fc[0]
                newx = sc[1]
                newy = sc[0]
                if chessBoard[oldx][oldy] != None and chessBoard[oldx][oldy].color == turn:
                    i = 0
                    found = False
                    for i in range(0, len(moves) ):
                        if moves[i][1] == oldx and moves[i][2] == oldy and moves[i][3] == newx and moves[i][4] == newy:
                            found = True
                            index = i
                            break
                    if found:
                        movepiece(chessBoard, moves[i][0], moves[i][1], moves[i][2], moves[i][3], moves[i][4])
                        moves_list.insert(0, "W "+chessBoard[newx][newy].typ+" "+moveToStr(oldx, oldy, newx, newy) )

                        
                        pygame.time.delay(100)
                        
                        st, mv = get(turn, chessBoard)
                        if st == 1:
                            status = "Checked"
                        else:
                            status = ""
                        turn = "Black"
                        one_time_white = True
                        fc = None
                        sc = None
                    else:
                        sc = None
                        fc = None
                else:
                    fc = None
                    sc = None
pygame.draw.rect(screen, (1, 20, 15), (520, 395, 100, 100))

pygame.display.update()

pygame.quit()