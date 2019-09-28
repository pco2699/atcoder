def D():
    n, m = map(int, input().split())
    a, b, c = [], [], []
    dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

    for _ in range(m):
        in_a, in_b, in_c = map(int, input().split())
        a.append(in_a - 1)
        b.append(in_b - 1)
        c.append(in_c)

    for i in range(m):
        dist[a[i]][b[i]] = min(dist[a[i]][b[i]], c[i])
        dist[b[i]][a[i]] = min(dist[b[i]][a[i]], c[i])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    ans = m
    for i in range(m):
        shortest = False
        for j in range(n):
            if dist[j][a[i]] + c[i] == dist[j][b[i]]:
                shortest = True
                break
        if shortest:
            ans -= 1

    print(ans)


if __name__ == '__main__':
    D()


