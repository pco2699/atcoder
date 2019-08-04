from copy import deepcopy

def main():
    n = int(input())
    p = list(map(int,input().split()))
    org = deepcopy(p)
    p.sort()

    count = 0

    for i in range(n):
        if p[i] != org[i]:
            count += 1

    if count <= 2:
        print("YES")
    else: 
        print("NO")


if __name__ == "__main__":
    main()

