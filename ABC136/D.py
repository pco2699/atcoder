def main():
    S = input()
    N = len(S)
    res = [0] * N
    for i in range(N-1):
        if S[i] == 'R' and S[i+1] == 'L':
            l, r, cnt = i, i+1, 0
            while l >= 0 and S[l] == 'R':
                if cnt % 2 == 0:
                    res[i] += 1
                else:
                    res[i+1] += 1
                cnt += 1
                l -= 1

            cnt = 0
            while r < N and S[r] == 'L':
                if cnt % 2 == 0:
                    res[i+1] += 1
                else:
                    res[i] += 1
                cnt += 1
                r += 1
    print(" ".join([str(r) for r in res]))

if __name__ == "__main__":
    main()