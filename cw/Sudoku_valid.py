def validSolution(board):
    def set(arr, n):
        if not (n < 0 or n > len(arr)):
            nums[n] = 1

    def set_filled(arr):
        return all(n for n in arr)

    for i in range(len(board)):
        nums = [0] * 9
        for j in range(len(board[0])):
            set(nums, board[i][j] - 1)
        if not set_filled(nums):
            return False
                
    for i in range(len(board)):
        nums = [0] * 9
        for j in range(len(board[0])):
            set(nums, board[j][i] - 1)
        if not set_filled(nums):
            return False
                
    for i in range(0, len(board), 3):
        for j in range(0, len(board[0]), 3):
            nums = [0] * 9
            for k in range(3):
                for l in range(3):
                    set(nums, board[i+k][j+l] - 1)
        if not set_filled(nums):
            return False

    return True
