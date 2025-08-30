"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
VALUE = "V"
active_player = "X"

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    
    if active_player == "X":
        active_player = "O"
        return "O"
    else:
        active_player = "X"
        return "X"

def actions(board):
    # Return list of tuple coordinates for available moves.
    action_list = []
    row = 0
    for row in board:
        column = 0
        for r in row:
            if r is None:
                action_list.append((row, column))
            column += 1
        row += 1
        


def result(board, action):
    # take an action (a tuple coordinate) and update a copy of board
    deep = copy.deepcopy(board)

    board_location = board[action[0],action[1]]
    
    if board_location is None:
        raise Exception ("Invalid Move")
    
    # Update coordinate with the active player X or O
    board_location = active_player

    return board


def winner(board):

    # Test if there is a winner or a draw
    # Winner in rows? 
    for i in range(2):
        if all(x == board[i][0] for x in board[i]):
            return active_player
    
    # Winner in Columns?
    for i in range(2):
        if board[0][i] == board[1][i] & board[0][i] == board[2][i]:
            return active_player
        
    # Winner in Diagonals?
    if board [0][0] == board[1][1] & board[0][0] == board[2][2]:
        return active_player
    if board [0][2] == board[1][1] & board[0][2] == board[2][0]:
        return active_player
    
    return None


def terminal(board):
    # Check if there is a winner
    if winner(board) != None:
        return True
    # Check if any empty cells
    count_empty = sum(cell is None for row in board for cell in row)
    if count_empty == 0:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
