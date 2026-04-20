import math

vals = list(map(int, input("Enter leaf nodes: ").split()))

def ab(d, node, maxi, a, b):
    if d == 3:
        return vals[node]

    if maxi:
        v = -math.inf
        for i in range(2):
            v = max(v, ab(d+1, node*2+i, False, a, b))
            a = max(a, v)
            if b <= a:
                break
        return v
    else:
        v = math.inf
        for i in range(2):
            v = min(v, ab(d+1, node*2+i, True, a, b))
            b = min(b, v)
            if b <= a:
                break
        return v

print("Result:", ab(0, 0, True, -math.inf, math.inf))