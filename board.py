from copy import deepcopy

def empty_board():
    board = [[None, None, None], [None, None, None], [None, None, None]]
    return board

def winner(board):
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            return board[0][i]
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0]:
        return board[2][0]

def terminal(board):
    if winner(board):
        return True
    
    for x in range(3):
        for y in range(3):
            if board[x][y] is None:
                return False
    return True

def player(board):
    x_count = 0
    o_count = 0
    for i in range(0,3):
       for j in range(0, 3):
            if board[i][j] == 'X':
               x_count += 1
            elif board[i][j] == 'O':
               o_count += 1

    if x_count > o_count:
        return "O" 
    else:
        return "X"

def move(board, pos):
    r, c = pos
    if board[r][c]:
        return board
    new_board = deepcopy(board)
    new_board[r][c] = player(board)
    return new_board
