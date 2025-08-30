"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
VALUE = "V"

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    if x_count <= o_count:
        return "X"
    else:
        return "O"

def actions(board):
    # Return list of tuple coordinates for available moves.
    action_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                action_list.append((i, j))
    return action_list
        

def result(board, action):
  # Make a deep copy of the board so we don’t overwrite the original
    deep = copy.deepcopy(board)

    # Check if the chosen cell is already occupied (invalid move)
    if deep[action[0]][action[1]] is not None:
        raise Exception("Invalid Move")

    # Place the current player's mark (X or O) on the copied board
    # We pass the board into player() so it figures out whose turn it is
    deep[action[0]][action[1]] = player(board)

    # Return the new board with the move applied
    return deep


def winner(board):
    for row in range(3):
        if board[row][0] is not None and board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]

    # Check columns
    for col in range(3):
        if board[0][col] is not None and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Check diagonals
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def terminal(board):
    # Check if there is a winner
    if winner(board) != None:
        return True
    # Check if any empty cells
    count_empty = sum(cell is EMPTY for row in board for cell in row)
    if count_empty == 0:
        return True
    
    return False


def utility(board):
    # Minmax score
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    available_cells = actions(board)

    # if X we want max score
    if player(board) == "X":
        best_score = -2
        best_move = None
        for action in actions(board):
            move_score = min_score(result(board, action))
            print(action, move_score)            
            if move_score > best_score:
                best_score = move_score
                best_move = action
        print("--------")                
        return best_move

    # if O we want min score
    if player(board) == "O":
        best_score = 2
        best_move = None
        for action in actions(board):
            move_score = max_score(result(board, action))
            print(action, move_score)
            if move_score < best_score:
                best_score = move_score
                best_move = action
        print("--------")
        return best_move

def min_score(board):
    if terminal(board):
        return utility(board)   
    value = 2
    for action in actions(board):
        value = min(value, max_score(result(board, action)))
    return value
    
def max_score(board):
    if terminal(board):
        return utility(board) 
    value = -2
    for action in actions(board):
        value = max(value, min_score(result(board,action)))
    return value