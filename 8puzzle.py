+from collections import deque

goal = '123456780'


def print_board(s):
    for i in range(0, 9, 3):
        print(' '.join(s[i:i+3]))
    print()


def neighbors(s):
    i = s.index('0')
    moves = []
    swap = [(1,3),(0,2,4),(1,5),(0,4,6),(1,3,5,7),(2,4,8),(3,7),(4,6,8),(5,7)]
    for j in swap[i]:
        lst = list(s)
        lst[i], lst[j] = lst[j], lst[i]
        moves.append(''.join(lst))
    return moves


def bfs(start):
    q = deque([(start, [start])])  
    seen = set([start])
    
    while q:
        state, path = q.popleft()
        
        if state == goal:
            print(f"Steps: {len(path)-1}\n")
            print("Solution Path:\n")
            for step in path:
                print_board(step)
            return
        
        for n in neighbors(state):
            if n not in seen:
                seen.add(n)
                q.append((n, path + [n]))


bfs('461253078')
