def hanoi(n):
    if n == 1:
        return 1
    else:
        return hanoi(n-1) + 1 + hanoi(n-1)


print("횟수 :", hanoi(int(input('탑의 높이 : '))))


def hanoi_2(n, start, mid, end):
    if n == 1:
        print(n, start + " -> " + end)

    else:
        hanoi_2(n-1, start, end, mid)
        print(n, start + " -> " + end)
        hanoi_2(n-1, mid, start, end)


hanoi_2(int(input('탑의 높이 : ')), "A", "B", "C")
