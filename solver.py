
def solve(board):
    find = find_empty(board)

    # Base Case: if board is full
    if not find:
        return True
    else:
        row, col = find

    # Recusive Case
    for num in range(1, 10):
        if valid(board, num, find):  # Constraint
            board[row][col] = num  # Choose
            if solve(board):  # Explore
                return True
            board[row][col] = 0  # Un Choose
    return False


def valid(board, num, pos):
    row, col = pos

    # Check row
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False

    # Check col
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    # Check box
    box_x = col//3
    box_y = row//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # Row and col
    return None


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- -"*8)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:

                print(board[i][j])

            else:
                print(str(board[i][j])+" ", end="")
