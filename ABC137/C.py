def main():
    n = int(input())
    strings =[input() for i in range(n)]

    ans = {}
    count = 0
    for s in strings:
        c = tuple(sorted(s))
        if c in ans:
            count += ans[c]
            ans[c] = ans[c] + 1
        else:
            ans[c] = 1

    print(count)

if __name__ == "__main__":
    main()