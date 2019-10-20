def a():
    a_, b = map(int, input().split())
    res = a_ - b * 2
    print(res if res > 0 else 0)


if __name__ == '__main__':
    a()