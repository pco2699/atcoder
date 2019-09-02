def c():
    n = int(input())
    hs = list(map(int, input().split()))

    if n <= 1:
        print(0)
        return

    max_count, count = 0, 0
    for i in range(1, n):
        if hs[i] <= hs[i-1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0

    max_count = max(max_count, count)
    print(max_count)


if __name__ == '__main__':
    c()
