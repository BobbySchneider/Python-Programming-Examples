# In this file you are required to implement the following functions:
#
# 1) generateChildren(self) - a function that generates the children of the board
#    The list of the generated children must have a specific format.
#    For each child the format is (move to generate this child, child object).
#    ATTENTION: this method is different from the one you implemented in hw1!
#
# 2) def miniMax(self, board, depth, player) - a helper function
#    that implements the minimax algorithm.
#
# 3) def alphaBeta(self, board, depth, player, alpha, beta) - a function
#    that implements the alpha beta pruning algorithm.


import math
from board import Board
import random


# This is the parent class for your AI bots.
class Bot:

    def __init__(self, depthLimit, isPlayerOne):
        self.isPlayerOne = isPlayerOne
        self.depthLimit = depthLimit

    # return a list of children and moves that generate them
    def generateChildren(self, board):
        children = []
        # ATTENTION: this method is different from the one you implemented in hw1!
        # iterate through each column
            # if a column is not full:
                # 1) make a copy of the board (HINT: new_board = Board(board))
                # 2) make a move in column i, thus generating a child
                #    (HINT: you need to use makeMove() function from the Board class)
                # 3) append a tuple (move, child_board) to the list
        #
        # NOTE: this list must be in order (i.e. [[0, child_0], [1, child_1], ...])
        #
        #######################################################################
        #######################################################################
        #######################################################################
        #
        # TODO: add your code here

        for i in range(board.width):
            if len(board.board[i]) < board.height: #if col not full
                
                new_board = Board(board) #copy new board
                new_board.makeMove(i) #make move

                temp = (i, new_board)
                children.append(temp) #append tuple

        return children

# In this class you are required to implement the  minimax algorithm
class minMaxBot(Bot):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # return the optimal column to move in
    def findMove(self, board):
        score, move = self.miniMax(board, self.depthLimit, self.isPlayerOne)
        return move

    # findMove helper function - minimax
    def miniMax(self, board, depth, player):
        # this function returns a tuple (score, move)
        # 1) if the board is in a final state (0,1 or 2), return heuristic.
        #    We don't care to return a move, so we can just return -1.
        # 2) if depth is 0, return the heuristic.
        #    We don't care to return a move, so we can just return -1.
        # 3) implement miniMax algorithm
        #
        # To check if the state is terminal, use isGoal() function
        # from the class Board: board.isGoal()
        #
        # To get the heuristic for the board, use the heuristic() function
        # from the class Board: board.heuristic()
        #
        # Remember to follow the rule: positive is good for Player 1,
        # negative is good for Player 2.
        #
        # You will have to generate children for the board,
        # and recursively call miniMax().
        # This must be done in order (i.e. col. 0, 1, etc.)
        #
        # You can use -math.inf for negative infinity
        # and math.inf for positive infinity.
        #
        #######################################################################
        #######################################################################
        #######################################################################
        #
        # TODO: add your code here

        if board.isGoal() >= 0: # check goal
            return (board.heuristic(), -1)

        if depth == 0: #check if depth at 0
            return (board.heuristic(), -1)

        # implement minimax here
        negInf = -math.inf
        posInf = math.inf

        if player == True: #check for player 1
            bestScore = negInf
            children = self.generateChildren(board)

            for child in children:
                move = child[0]
                score = self.miniMax(child[1], depth - 1, False)[0]

                if score > bestScore:
                    bestScore = score
                    bestMove = move

            return (bestScore, bestMove)
            
        else: #else it's player 2
            bestScore = posInf
            children = self.generateChildren(board)

            for child in children:
                move = child[0]
                score = self.miniMax(child[1], depth - 1, True)[0]

                if score < bestScore:
                    bestScore = score
                    bestMove = move
            
            return (bestScore, bestMove)


# In this class you are required to implement the alpha beta pruning algorithm
class alphaBetaBot(Bot):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # returns the optimal column to move in
    def findMove(self, board):
        score, move = self.alphaBeta(board, self.depthLimit, self.isPlayerOne, -math.inf, math.inf)
        return move

    # findMove helper function - alpha beta pruning
    def alphaBeta(self, board, depth, player, alpha, beta):
        # this function returns a tuple (score, move)
        # 1) if the board is in a final state (0,1 or 2), return heuristic.
        #    We don't care to return a move, so we can just return -1.
        # 2) if depth is 0, return the heuristic.
        #    We don't care to return a move, so we can just return -1.
        # 3) implement miniMax algorithm
        #
        # To check if the state is terminal, use isGoal() function
        # from the class Board: board.isGoal()
        #
        # To get the heuristic for the board, use the heuristic() function
        # from the class Board: board.heuristic()
        #
        # Remember to follow the rule: positive is good for Player 1,
        # negative is good for Player 2.
        #
        # You will have to generate children for the board,
        # and recursively call alphaBeta().
        # This must be done in order (i.e. col. 0, 1, etc.)
        #
        # You can use -math.inf for negative infinity
        # and math.inf for positive infinity.
        #
        # You can use max(x, y) and min (x, y) functions to find
        # maximum/minimum of two values.
        #
        # Your code must prune suboptimal nodes.
        #
        #######################################################################
        #######################################################################
        #######################################################################
        #
        # TODO: add your code here

        ###
        ### RECEIVED TA HELP FROM ALEX RUBIN ON THIS FUNCTION ### 
        ###

        if depth == 0: #check if depth at 0
            return (board.heuristic(), -1)

        if board.isFull(): #check for full state
            return (board.heuristic(), -1)

        if board.isGoal() == 0 or board.isGoal() == 1 or board.isGoal() == 2: #check goal
            return (board.heuristic(), -1)

        # implement alphabeta here
        negInf = -math.inf
        posInf = math.inf

        if player == True: #check for player 1
            bestScore = negInf
            children = self.generateChildren(board)
            
            for child in children:
                move = child[0]
                score = self.alphaBeta(child[1], depth - 1, False, alpha, beta)[0]

                if score > bestScore:
                    bestScore = score
                    bestMove = move

                alpha = max(alpha, bestScore)

                if alpha >= beta:
                    break

            return (bestScore, bestMove)

        else: #else it's player 2
            bestScore = posInf
            children = self.generateChildren(board)

            for child in children:
                move = child[0]
                score = self.alphaBeta(child[1], depth - 1, True, alpha, beta)[0]

                if score < bestScore:
                    bestScore = score
                    bestMove = move

                beta = min(beta, bestScore)

                if beta <= alpha:
                    break
            
            return (bestScore, bestMove)



# random bot
class randomBot(Bot):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # return a random column to move in
    def findMove(self, board):
        move = random.randint(0, board.width - 1)
        while len(board.board[move]) == board.height:
            move = random.randint(0, board.width - 1)
        return move

# human player
class HumanPlayer:

    def __init__(self, depthLimit, isPlayerOne):
        pass

    def findMove(self, board):
        pass
