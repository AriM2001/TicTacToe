"""
Tic Tac Toe Player

Group: Jose Fuentes, Ari Montes, Daniel Peralta, Perry Wang
This module contains all of the logic for playing the game, and for making optimal moves.
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount, oCount = 0, 0
    for i in board:
        #print("row", row)
        for j in i:
            if j == "X":
                xCount += 1
            elif j == "O":
                oCount += 1
    if xCount > oCount:
        return "O"
    elif xCount < oCount:
        return "X"
    return "X" ##bug
    #print("board", board)
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.append((i, j))
    return set(actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == None or action[0] > 2 or action[1] > 2:
        raise Exception("action does not exist")
    temp = copy.deepcopy(board)
    temp[action[0]][action[1]] = player(temp)
    #print(board)
    return temp


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #for loop checks the rows and columns for a winner
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    #remaining 2 if statements check the diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if actions(board) == set() or winner(board) != None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
        
    def max_value(board):
        # Check if the game over and return utility value
        if terminal(board):
            return utility(board)
        v = -math.inf
        # Iterate over all actions and choose the one with the maximum value
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        # Check if the game is over and return the utility value
        if terminal(board):
            return utility(board)
        v = math.inf
        # Iterate over all actions and choose the one with the minimum value
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    # Determine the current player and choose the optimal action
    if player(board) == "X":
        v = -math.inf
        for action in actions(board):
            temp = min_value(result(board, action))
            if temp > v:
                v = temp
                bestAction = action
    else:
        v = math.inf
        for action in actions(board):
            temp = max_value(result(board, action))
            if temp < v:
                v = temp
                bestAction = action
    return bestAction
    

    
        
#test = [["X", "O", "O"],
        #["O", "O", "X"],
        #["X", "X", EMPTY]]
#test = [["O", EMPTY, EMPTY],
        #["X", "X", "X"],
        #[EMPTY, EMPTY, "O"]]
#test = [["O", "X", "O"], ["X", "O", "O"], ["O", "X", "X"]]
#print(player(test))
#print(actions(test))
#print(result(test, (0, 1)))
#print(result(test, (3, 1)))
#print(winner(test))
#print(utility(test))
#print(terminal(test))
#print(minimax(test))