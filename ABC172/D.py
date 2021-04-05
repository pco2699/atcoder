N = int(input())

dp = [0] * N

for i in range(1, N+1):
    for j in range(1, N // i + 1):
        dp[j*i-1] += 1
ans = 0
for i, d in enumerate(dp):
    ans += (i+1) * d

print(ans)
