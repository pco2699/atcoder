def e():
    n, m, l = map(int, input().split())
    dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
    fuel = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

    for i in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = c
        dist[b][a] = c

    q = int(input())
    li_st = []
    for i in range(q):
        s, t = map(int, input().split())
        li_st.append([s, t])

    for k in range(n):
        for i in range(n):from bisect import bisect_right


def d():
    n = int(input())
    ls = list(map(int, input().split()))
    ls.sort()
    count = 0
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            k = bisect_right(ls, ls[i]-ls[j])
            if j >= k:
                count += j - k

    print(count)


if __name__ == '__main__':
    d()

            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if dist[i][j] <= l:
                fuel[i][j] = min(1, fuel[i][j])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                fuel[i][j] = min(fuel[i][j], fuel[i][k] + fuel[k][j])

    for s, t in li_st:
        s -= 1
        t -= 1
        if fuel[s][t] == float('inf'):
            print(-1)
        else:
            print(fuel[s][t] - 1)


if __name__ == '__main__':
    e()
