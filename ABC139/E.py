"""
まだ途中
"""
def e():
    n = int(input())
    player_orders = []
    for _ in range(n):
        player_orders.append(list(map(int, input().split())))

    schedule = [[0] * n] * n

    for p in range(n):
        for i in range(n):
            opponent = player_orders[p][i]






if __name__ == '__main__':
    e()