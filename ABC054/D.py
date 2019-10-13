def d():
    nmax, mmax = 40, 10
    n, ma, mb = map(int, input().split())
    a, b, c = [], [], []
    for i in range(n):
        a_, b_, c_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
        c.append(c_)

    dp = [[[float('inf') for _ in range(n*mmax+1)] for _ in range(n*mmax+1) ] for _ in range(n+1)]
    dp[0][0][0] = 0

    for i in range(n):
        for ca in range(n*mmax+1):
            for cb in range(n*mmax+1):
                if dp[i][ca][cb] == float('inf'):
                    continue
                dp[i+1][ca][cb] = min(dp[i+1][ca][cb], dp[i][ca][cb])
                if ca + a[i] < n*mmax+1 and cb + b[i] < n*mmax+1:
                    dp[i+1][ca + a[i]][cb + b[i]] = min(dp[i+1][ca + a[i]][cb + b[i]], dp[i][ca][cb] + c[i])

    ans = float('inf')
    for ca in range(1, n*mmax+1):
        for cb in range(1, n*mmax+1):
            if ma * cb == mb * ca:
                ans = min(ans, dp[n][ca][cb])

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    d()
