from itertools import accumulate

def main():
    N, K = map(int,input().split())
    A = list(map(int,input().split()))

    S = sum(A)
    divisors = make_divisors(S)
    
    for d in divisors:
        R = list(map(lambda x: x % d, A))
        R = [r for r in R if r != 0]
        R.sort()
        cnt_m, cnt_p = 0, 0
        for r in R:
            if cnt_m <= K - r:
                cnt_m += r
            else:5
                cnt_p += d - r
        if cnt_m <= K and cnt_p <= K:
            print(d)
            exit()

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors

if __name__ == "__main__":
    main()