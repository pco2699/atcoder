import itertools


def b():
    n = map(int, input())
    ds = list(map(int, input().split()))
    cs = list(itertools.combinations(ds, 2))

    sum_ = 0

    for c in cs:
        sum_ += c[0] * c[1]

    print(sum_)


if __name__ == '__main__':
    b()
