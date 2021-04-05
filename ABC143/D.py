from bisect import bisect_right


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
