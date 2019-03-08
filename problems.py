from node import Node

import math
import copy


class FifteensNode(Node):
    """appends the Node class to solve the 15 puzzle.

    Parameters
    ----------
    parent : Node, optional
        The parent node. It is optional only if the input_str is provided. Default is None.

    g : int or float, optional
        The cost to reach this node from the start node : g(n).
        In this puzzle it is the number of moves to reach this node from the initial configuration.
        It is optional only if the input_str is provided. Default is 0.

    board : list of lists
        The two-dimensional list that describes the state. It is a 4x4 array of values 0, ..., 15.
        It is optional only if the input_str is provided. Default is None.

    input_str : str
        The input string to be parsed to create the board.
        The argument 'board' will be ignored, if input_str is provided.
        Example: input_str = '1 2 3 4\n5 6 7 8\n9 10 0 11\n13 14 15 12' # 0 represents the empty cell

    Examples
    ----------
    Initialization with an input string (Only the first/root construction call should be formatted like this):
    >>> n = FifteensNode(input_str=initial_state_str)
    >>> print(n)
      5  1  4  8
      7     2 11
      9  3 14 10
      6 13 15 12

    Generating a child node (All the child construction calls should be formatted like this) ::
    >>> n = FifteensNode(parent=p, g=p.g+c, board=updated_board)
    >>> print(n)
      5  1  4  8
      7  2    11
      9  3 14 10
      6 13 15 12

    """

    def __init__(self, parent=None, g=0, board=None, input_str=None):
        # NOTE: You shouldn't modify the constructor
        if input_str:
            self.board = []
            for i, line in enumerate(filter(None, input_str.splitlines())):
                self.board.append([int(n) for n in line.split()])
        else:
            self.board = board

        super(FifteensNode, self).__init__(parent, g)


    def generate_children(self):
        """Generates children by trying all 4 possible moves of the empty cell.

        Returns
        -------
            children : list of Nodes
                The list of child nodes.
        """

        # TODO: add your code here
        # You should use self.board to produce children. Don't forget to create a new board for each child
        # e.g you can use copy.deepcopy function from the standard library.
        # pass

        '''
        Find position
        iterate over possible values
        deep copy each new board

        '''

        current = self
        children = []

        i = 0
        j = 0
        k = 0
        s = current.state

        for value in s: # find index
            if value == 0:
                break
            else:
                k += 1
        
        i = math.floor(k / 4) # calculate y coordinate
        j = (k % 4) # calculate x coordinate

        firstCopy = copy.deepcopy(current)
        secondCopy = copy.deepcopy(current)
        thirdCopy = copy.deepcopy(current)
        fourthCopy = copy.deepcopy(current)

        if i-1 > -1:
            temp = current.board[i-1][j]
            firstCopy.board[i][j] = temp
            firstCopy.board[i-1][j] = 0
            n = FifteensNode(parent=current, g=current.g + 1, board=firstCopy.board)
            children.append(n)

        if i+1 < 4:
            temp = current.board[i+1][j]
            secondCopy.board[i][j] = temp
            secondCopy.board[i+1][j] = 0
            n = FifteensNode(parent=current, g=current.g + 1, board=secondCopy.board)
            children.append(n)

        if j-1 > -1:
            temp = current.board[i][j-1]
            thirdCopy.board[i][j] = temp
            thirdCopy.board[i][j-1] = 0
            n = FifteensNode(parent=current, g=current.g + 1, board=thirdCopy.board)
            children.append(n)

        if j+1 < 4:
            temp = current.board[i][j+1]
            fourthCopy.board[i][j] = temp
            fourthCopy.board[i][j+1] = 0
            n = FifteensNode(parent=current, g=current.g + 1, board=fourthCopy.board)
            children.append(n)
        

        if len(children) > 0:
            return children
        else:
            return []
         

    def is_goal(self):
        """Decides whether this search state is the final state of the puzzle.

        Returns
        -------
            is_goal : bool
                True if this search state is the goal state, False otherwise.
        """

        current = self.board
        correctList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 0]
        myList = []

        for i in range(0,4):
            for j in range(0,4):
                myList.append(current[i][j])

        i = 0
        for a in myList:
            if (a != correctList[i]):
                return False
            
            i += 1
        return True


    def evaluate_heuristic(self):
        """Heuristic function h(n) that estimates the minimum number of moves
        required to reach the goal state from this node.

        Returns
        -------
        h : int or float
                The heuristic value for this state.
        """

        # TODO: add your code here
        # You may want to use self.board here.
        # pass

        if self.is_goal(): # check if goal state already
            return 0

        manhattan = 0 # variable we want to return
        current = self.board

        correctPos = [[0,0], [0,1], [0,2], [0,3], [1,0], [1,1], [1,2], [1,3], [2,0], [2,1], [2,2], [2,3], [3,0], [3,1], [3,2], [3, 3]]
        correctVal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

        #start
        x = -1
        i = -1
        for b in current:
            y = -1
            x += 1
            for a in b:
                i += 1
                y += 1
                if current[x][y] != correctVal[i]:
                    print(a)
                    print(correctVal[i])
                    print(correctPos[i][0])
                    print(x)
                    manhattan += abs(correctPos[i][0] - x)
                    manhattan += abs(correctPos[i-1][1] - y)
                    print(manhattan)

        #print(manhattan)
        return manhattan


    def _get_state(self):
        """Returns an hashable representation of this search state.

        Returns
        -------
            state: tuple
                The hashable representation of the search state
        """
        # NOTE: You shouldn't modify this method.
        return tuple([n for row in self.board for n in row])

    def __str__(self):
        """Returns the string representation of this node.

        Returns
        -------
            state_str : str
                The string representation of the node.
        """
        # NOTE: You shouldn't modify this method.
        sb = []  # String builder
        for row in self.board:
            for i in row:
                sb.append(' ')
                if i == 0:
                    sb.append('  ')
                else:
                    if i < 10:
                        sb.append(' ')
                    sb.append(str(i))
            sb.append('\n')
        return ''.join(sb)


class SuperqueensNode(Node):
    """appends the Node class to solve the Superqueens problem.

    Parameters
    ----------
    parent : Node, optional
        The parent node. Default is None.

    g : int or float, optional
        The cost to reach this node from the start node : g(n).
        In this problem it is the number of pairs of superqueens that can attack each other in this state configuration.
        Default is 1.

    queen_positions : list of pairs
        The list that stores the x and y positions of the queens in this state configuration.
        Example: [(q1_y,q1_x),(q2_y,q2_x)]. Note that the upper left corner is the origin and y increases downward
        Default is the empty list [].
        ------> x
        |
        |
        v
        y

    n : int
        The size of the board (n x n)

    Examples
    ----------
    Initialization with a board size (Only the first/root construction call should be formatted like this):
    >>> n = SuperqueensNode(n=4)
    >>> print(n)
         .  .  .  .
         .  .  .  .
         .  .  .  .
         .  .  .  .

    Generating a child node (All the child construction calls should be formatted like this):
    >>> n = SuperqueensNode(parent=p, g=p.g+c, queen_positions=updated_queen_positions, n=p.n)
    >>> print(n)
         Q  .  .  .
         .  .  .  .
         .  .  .  .
         .  .  .  .

    """

    def __init__(self, parent=None, g=0, queen_positions=[], n=1):
        # NOTE: You shouldn't modify the constructor
        self.queen_positions = queen_positions
        self.n = n
        super(SuperqueensNode, self).__init__(parent, g)

    def generate_children(self):
        """Generates children by adding a new queen.

        Returns
        -------
            children : list of Nodes
                The list of child nodes.
        """
        # TODO: add your code here
        # You should use self.queen_positions and self.n to produce children.
        # Don't forget to create a new queen_positions list for each child.
        # You can use copy.deepcopy function from the standard library.
        # pass

        
        

    def is_goal(self):
        """Decides whether all the queens are placed on the board.

        Returns
        -------
            is_goal : bool
                True if all the queens are placed on the board, False otherwise.
        """
        # You should use self.queen_positions and self.n to decide.
        # TODO: add your code here
        # pass

        currentQueens = self.queen_positions
        currentn = self.n
        x = 0
        y = 0

        for i in currentQueens: # start iteration over queen positions
            x = i[0]
            y = i[1]
            numofQueens = 0

            for queen in currentQueens: # compare other queens to current
                a = queen[0]
                b = queen[1]

                if x == a or y == b: # check if other queens in same column or row ***HARD CONSTRAINT***
                    numofQueens += 1
                if numofQueens > 1: 
                    return False


        # check that all rows and columns have exactly one queen ***CHECK ALL QUEENS HAVE BEEN PLACED***
        rowdic = {}
        coldic = {}
        # init row and col dictionary
        for i in range(0, currentn):
            rowdic[i: 0]
        for i in range(0, currentn):
            coldic[i: 0]

        for i in currentQueens: # iterate 
            x = i[0]
            y = i[1]

            rowdic[y] += 1 # update how many queens on column y
            coldic[x] += 1 # update how many queens on row x

        for row in rowdic: # check to make sure exactly one queen in every row
            if rowdic[row] != 1:
                return False

        for col in coldic: # check to make sure exactly one queen in very column
            if coldic[col] != 1:
                return False

        return True


    def evaluate_heuristic(self):
        """Heuristic function h(n) that estimates the minimum number of conflicts required to reach the final state.

        Returns
        -------
            h : int or float
                The heuristic value for this state.
        """
        # If you want to design a heuristic for this problem, you should use self.queen_positions and self.n.
        # TODO: add your code here (optional)
        return 0

    def _get_state(self):
        """Returns an hashable representation of this search state.

        Returns
        -------
            state: tuple
                The hashable representation of the search state
        """
        # NOTE: You shouldn't modify this method.
        return tuple(self.queen_positions)

    def __str__(self):
        """Returns the string representation of this node.

        Returns
        -------
            state_str : str
                The string representation of the node.
        """
        # NOTE: You shouldn't modify this method.
        sb = [[' . '] * self.n for i in range(self.n)]  # String builder
        for i, j in self.queen_positions:
            sb[i][j] = ' Q '
        return '\n'.join([''.join(row) for row in sb])
