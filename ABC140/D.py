def d():
    N, K = map(int,input().split())
    S = list(input())
    happiness = 0

    for i in range(N-1):
        if S[i] == S[i+1]:
            happiness += 1

    print(min(happiness+2*K, N-1))


if __name__ == '__main__':
    d()
