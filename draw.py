def draw_line(n: int):
    print(n* "-")

def new_lines(n: int):
    for _ in range(n):
        print()

def draw_space(n=0):
    for _ in range(n):
        print(" ", end='')
    print()

def draw_empty_cell(space: int):
    for _ in range(space):
        print(' ', end='')

    print("|", end='')

def draw_cell(space: int, char: str):
    for _ in range(space//2):
        print(' ', end='')
    
    print(char, end='')

    for _ in range(space//2):
        print(' ', end='')
    
    print("|", end='')

def draw_char(space: int, char: str):
    for _ in range(space//2):
        print(' ', end='')
    
    print(char, end='')
    print()

def draw_empty_row():
    draw_empty_cell(5)
    draw_empty_cell(5)
    print()

def draw_row(row):
    if row[0] and row[1] and row[2]:
        draw_cell(5, row[0])
        draw_cell(5, row[1])
        draw_char(5, row[2])
        return

    if row[0] and row[1]:
        draw_cell(5, row[0])
        draw_cell(5, row[1])
        print()
        return
    
    if row[1] and row[2]:
        draw_empty_cell(5)
        draw_cell(5, row[1])
        draw_char(5, row[2])
        return

    if row[0] and row[2]:
        draw_cell(5, row[0])
        draw_empty_cell(5)
        draw_char(5, row[2])
        return
    
    if row[0]:
        draw_cell(5, row[0])
        draw_empty_cell(5)
        print()
        return
    
    if row[1]:
        draw_empty_cell(5)
        draw_cell(5, row[1])
        print()
        return
    
    if row[2]:
        draw_empty_cell(5)
        draw_empty_cell(5)
        draw_char(5, row[2])
        return

def draw_block(row):
    draw_empty_row()

    if row == [None, None, None]:
        draw_empty_row()
    else:
        draw_row(row)

    draw_empty_row()

def draw_board(board):
    new_lines(2)
    draw_block(board[0])
    draw_line(17)
    draw_block(board[1])
    draw_line(17)
    draw_block(board[2])
    new_lines(2)