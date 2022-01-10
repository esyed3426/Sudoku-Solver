# Sample sudoku base board state
sample_board = [[0, 0, 0, 7, 0, 0, 5, 0, 0], [0, 2, 9, 0, 3, 0, 0, 8, 0],
                [7, 1, 0, 6, 8, 0, 0, 0, 0], [0, 6, 7, 0, 0, 0, 3, 0, 5],
                [9, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 3, 0, 0, 0, 7, 9],
                [6, 4, 2, 8, 0, 3, 0, 1, 7], [3, 7, 0, 4, 0, 9, 2, 5, 8],
                [0, 0, 0, 2, 0, 1, 6, 0, 0]]


# Create a function for displaying the board
def display_board(board):
    for i in range(len(board)):
        # print a separator every three rows but not on the top line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                # if it is the last element, dont add a space
                print(board[i][j])
            else:
                # add a space and continue on the same line
                print(f"{board[i][j]} ", end=" ")


# Create a function to return an empty space
def find_space(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # the row and column
    return False


def valid_num(board, position, number):
    # position is of the form (row, column)
    # Check if the number is valid within the row
    for i in range(len(board)):
        if board[position[0]][i] == number and i != position[1]:
            return False

    # Check if the number is valid within the column
    for i in range(len(board)):
        if board[i][position[1]] == number and i != position[0]:
            return

    #Check if the number is valid within the 'box'
    x = position[1] // 3
    y = position[0] // 3

    # This will return a value in [0, 1, 2]
    # Check each value in the box
    for i in range(3 * y, 3 * y + 3):
        for j in range(3 * x, 3 * x + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


def solve(board):
    spot = find_space(board)
    if spot == False:
        return True
    else:
        row, column = spot

    #insert numbers
    for i in range(1, 10):
        if valid_num(board, (row, column), i):
            board[row][column] = i
            #if a solution can be found, then the solution is valid
            if solve(board):
                return True
            else:
                board[row][column] = 0
    return False


solve(sample_board)
display_board(sample_board)