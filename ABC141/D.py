import heapq


def d():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    h = []
    for i in range(N):
        heapq.heappush(h, -A[i])

    for _ in range(M):
        val = -1 * heapq.heappop(h)
        heapq.heappush(h, -1 * (val // 2))

    print(-1 * sum(h))


if __name__ == '__main__':
    d()
