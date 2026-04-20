def hanoi(n, a, b, c):
    if n==1:
        print(f"Move disk 1 from {a} to {c}")
        return

    hanoi(n-1, a, c, b)
    print(f"Move disk {n} from {a} to {c}")
    hanoi(n-1, b, a, c)

n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'B', 'C')