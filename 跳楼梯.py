dp=[0]*26
N=int(input())
dp[0]=1
for i in range(1,N+1):
    for j in range(i):
        dp[i]+=dp[j]
print(dp[N])
