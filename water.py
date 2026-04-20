A = int(input("enter capacity of jug A: "))
B = int(input("enter capacity of jug B: "))
target = int(input("enter target amount: "))

a = 0
b = 0

print("start state:", 0, 0)

while a != target and b != target:
    if b == 0:
        b = B
        print("fill jug B:", a, b)

    elif a == A:
        a = 0
        print("empty jug A:", a, b)

    else:
        transfer = min(b, A - a)
        a = a + transfer
        b = b - transfer
        print("pour B->A:", a, b)

print("target reached:", a, b)