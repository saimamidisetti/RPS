from board import *
from draw  import draw_board

def get_position(message):
    cell_pos = 20

    while cell_pos < 1 or cell_pos > 9:
        try:
            cell_pos = int(input(message))

        except ValueError:
            pass

        except KeyboardInterrupt:
            quit_key("Do you want to quit the game ? (press y ->)")
    
    row = (cell_pos - 1) // 3
    column = (cell_pos - 1) % 3
    return (row, column)

def quit_key(message):
    while True:
        try:
            key_pressed = input(message)
            key_pressed = key_pressed.lower()
            if key_pressed == 'y':
                exit()
            return

        except AttributeError:
            pass
        except KeyboardInterrupt:
            pass

def welcome_message():
    print("=== X === O === X ===")
    print("  Tic Tac Toe Game ")
    print("=== X ==== O === X ===")
    print("To quit press CTRL + C")


def game_play():
    welcome_message()
    board = empty_board()
    draw_board(board)

    while not terminal(board):
        pos = get_position(f'{player(board)} move (press (1 - 9) ->) ')
        board = move(board, pos)
        draw_board(board)
    
    if winner(board) == 'X':
        print("Winner is X")
    elif winner(board) == 'O':
        print("Winner is O")
    else:
        print("Draw!")

def main():
    game_play()


main()