from collections import defaultdict

def d():
    tree_map = defaultdict(list)
    value_map = defaultdict(int)
    N, Q = map(int,input().split())
 
    for _ in range(1, N):
        a, b = map(int,input().split())
        tree_map[a].append(b)

    for _ in range(1, Q+1):
        p, x = map(int,input().split())
        value_map[p] += x

    res = [0] * N
    stack = []
    stack.append((1, 0))
    while stack:
        i, s = stack.pop()
        if value_map[i] != 0:
            s += value_map[i]
        res[i-1] = s
        
        for j in tree_map[i]:
            stack.append((j, s))

    print(" ".join([str(r) for r in res]))


if __name__ == "__main__":
    d()

    
        




        
