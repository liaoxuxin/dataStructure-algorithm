# 01背包问题，https://www.acwing.com/problem/content/description/2/

N, V = map(int, input().split())
v = [0]
w = [0]
for i in range(N):
    a, b = map(int, input().split())
    v.append(a)
    w.append(b)

# 二维
# dp = [[0 for _ in range(V+1)] for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(1, V+1):
#         if j < v[i]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i]] + w[i])
# print(dp[N][V])

# 一维
dp = [0 for _ in range(V+1)]
for i in range(1, N+1):
    for j in range(v[i], V+1)[::-1]:
        dp[j] = max(dp[j], dp[j-v[i]] + w[i])
print(dp[V])
