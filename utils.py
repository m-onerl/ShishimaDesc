import os
import sys

sys.path.append('C:/Users/moner/Documents/Projekty/lab07/')

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
      0   1   2
      {board[0]}---{board[1]}---{board[2]}
      | \\ | / |
    3 {board[3]}--4{board[4]}4--{board[5]} 5
      | / | \\ |
      {board[6]}---{board[7]}---{board[8]}
      6   7   8
    ''')

def is_adjacent(pos1, pos2):
    connections = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }
    return pos2 in connections[pos1]

def valid_moves(pos, board):
    connections = {
        0: [1, 3, 4],
        1: [0, 2, 4],
        2: [1, 5, 4],
        3: [0, 6, 4],
        5: [2, 8, 4],
        6: [7, 3, 4],
        7: [6, 8, 4],
        8: [5, 7, 4],
        4: [0, 1, 2, 3, 5, 6, 7, 8]
    }
    return [conn for conn in connections[pos] if board[conn] == ' ']
