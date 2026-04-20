count = 1
board = ["_"*8 for _ in range(8)]
def backtrack(r):
    global count
    if r == 8:
        print("Solution", count)
        count += 1
        for row in board:
            print(" ".join(row))
        print()
        return
    for c in range(8):
        if all(board[i][c]=="_" and abs(c-board[i].find("Q"))!=r-i for i in range(r)):
            board[r] = board[r][:c] + "Q" + board[r][c+1:]
            backtrack(r+1)
            board[r] = "_"*8
backtrack(0)