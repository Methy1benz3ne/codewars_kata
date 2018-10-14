def validSolution(board):
    a = [0,0,0]
    a[0]=checkrow(board)
    a[1] = checkli(board)
    a[2] = checkrec(board)
    return a

def checkrow(board):
    board1 = board
    for i in range(9):
        board1[i].sort()
        if board1[i] != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True

def checkli(board):
    # newboard = zip(*board)
    # for row in newboard:
    #     if not check_one_to_nine(row):
    #         return False
    # return True
# def validate_cols(board):
    transposed = zip(*board)
    for row in transposed:
        if not check_one_to_nine(row):
            return False
    return True

def checkrec(board):
#     for i in range(0,9,3):
#         for j in range(0,9,3):
#             nums = board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]
#             if not check_one_to_nine(nums):
#                 return False
#     return True

# def validate_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if not check_one_to_nine(nums):
                return False
    return True


def check_one_to_nine(lst):
    check = range(1,10)
    return sorted(lst) == check

print(validSolution(([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]])))
