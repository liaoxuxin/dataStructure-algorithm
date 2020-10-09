# 多重背包，https://www.acwing.com/problem/content/description/4/
N, V = map(int, input().split())
v = [0]
w = [0]
n = 0
for i in range(N):
    a, b, c = map(int, input().split())
    v.extend([a] * c)
    w.extend([b] * c)
    n += c
N = n

dp = [0 for _ in range(V+1)]
for i in range(1, N+1):
    for j in range(v[i], V+1)[::-1]:
        dp[j] = max(dp[j], dp[j-v[i]] + w[i])
print(dp[V])
