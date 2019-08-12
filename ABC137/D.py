from heapq import heappush, heappop


def d():
    n, m = map(int,input().split())
    
    jobs = []
    for i in range(n):
        day, value = map(int,input().split())
        jobs.append((day, value))

    jobs.sort()
    
    cur, res = 0, 0
    h = []
    for i in range(1, m+1):
        while cur < n and jobs[cur][0] <= i:
            heappush(h, -jobs[cur][1])
            cur += 1
        if not h:
            continue
        res -= heappop(h)
 
    print(res)


if __name__ == "__main__":
    d()
