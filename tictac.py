#tictac
b = [" "]*9

def show():
    for i in range(0,9,3):
        print(b[i], "|", b[i+1], "|", b[i+2])

p = "X"
for _ in range(9):
    show()
    m = int(input(f"{p} pos(0-8): "))
    if b[m] == " ":
        b[m] = p
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        if any(b[x]==b[y]==b[z]==p for x,y,z in wins):
            show(); print(p,"wins"); break
        p = "O" if p=="X" else "X"
    else:
        print("Invalid")
        continue
else:
    show(); print("Draw")