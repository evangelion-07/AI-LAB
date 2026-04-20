def solveNQueens(n):
    res = []
    board = ["." * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append(board[:])
            return

        for c in range(n):
            if all(board[i][c] == "." and abs(c - board[i].find("Q")) != r - i for i in range(r)):
                board[r] = board[r][:c] + "Q" + board[r][c+1:]
                backtrack(r + 1)
                board[r] = "." * n

    backtrack(0)
    return res

n = int(input("Enter number of queens: "))
print(solveNQueens(n))