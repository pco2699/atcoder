def c():
    N = int(input())
    B = list(map(int, input().split()))

    if N <= 2:
        print(B[0] * 2)
        return
    sum = B[0]
    for i in range(1, N):
        if i == N-1:
            sum += B[N-2]
            break
        sum += min(B[i], B[i-1])

    print(sum)


if __name__ == '__main__':
    c()
