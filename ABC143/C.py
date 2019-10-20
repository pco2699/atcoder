def c():
    n = int(input())
    s = list(input())

    count = 1
    prev = s[0]

    for i in range(1, n):
        if prev == s[i]:
            continue
        count += 1
        prev = s[i]

    print(count)


if __name__ == '__main__':
    c()