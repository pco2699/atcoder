def e():
    n, m, p = map(int, input().split())

    edges = []
    for i in range(m):
        edges.append(tuple(map(int, input().split())))

    edges.sort(key=lambda x: x[1])
    dist = [float('inf') for i in range(n)]
    dist[0] = 0

    for i in range(n):
        for e in edges:
            if dist[e[1]-1] > dist[e[0]-1] - (e[2] - p):
                dist[e[1]-1] = dist[e[0]-1] - (e[2] - p)

    for i in range(n):
        for e in edges:
            if dist[e[1] - 1] > dist[e[0] - 1] - (e[2] - p):
                dist[e[1]-1] = float('-inf')

    if dist[n-1] == float('-inf'):
        print(-1)
    else:
        print(-dist[n-1] if -dist[n-1] >= 0 else 0)


if __name__ == '__main__':
    e()
