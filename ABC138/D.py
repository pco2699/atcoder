from collections import defaultdict
def d():
    tree_map = defaultdict(list)
    value_map = defaultdict(int)
    N, Q = map(int,input().split())
    
    for _ in range(1, N):
        a, b = map(int,input().split())
        tree_map[a].append(b)
        tree_map[b].append(a)

    res = [0] * N

    for _ in range(1, Q+1):
        p, x = map(int,input().split())
        res[p-1] += x
    
    stack = []
    stack.append((1, -1, 0))

    while stack:
        i, p, s = stack.pop()

        res[i-1] += s
        s = res[i-1]
        
        for j in tree_map[i]:
            if j == p:
                continue
            else:
                stack.append((j, i, s))

    print(*res)


if __name__ == "__main__":
    d()