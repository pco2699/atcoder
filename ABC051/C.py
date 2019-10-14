def c():
    sx, sy, tx, ty = map(int, input().split())
    dx = tx - sx
    dy = ty - sy

    # Path 1
    print("U" * dy + "R" * dx, end='')

    # Path 2
    print("D" * dy + "L" * dx, end='')

    # Path 3
    print("D" + "R" * (dx+1) + "U" * (dy+1) + "L", end='')

    # Path 4
    print("U" + "L" * (dx+1) + "D" * (dy+1) + "R", end='')


if __name__ == '__main__':
    c()
