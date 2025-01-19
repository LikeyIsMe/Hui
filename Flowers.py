#妈的更是题目都看不懂，这到底想干嘛。红花可以单独食用，但是白花必须成组食用。
t,k=map(int,input().split())
MOD=int(1e9+7)
dp=[0]*100001
#dp表示的是到达某一个位置的不同走法数，但是只使用dp就会超时，我们需要做一个辅助数组来表示从0到此位置所有的走法数
s=[0]*100001
dp[0]=1
s[0]=1
for i in range(1,100001):
    if i>=k:
        dp[i]=(dp[i-1]+dp[i-k])%MOD#跳楼梯，也就是要么吃一朵红花，要么吃一组白花
    else:
        dp[i]=dp[i-1]%MOD#位置不够吃白花，就只能吃红花
    s[i]=(s[i-1]+dp[i])%MOD
for _ in range(t):
    a,b=map(int,input().split())
    print(((s[b]-s[a-1])+MOD)%MOD)#不能用a，因为需要包括到a的方法数,在外面加MOD防止负数
    #看是看懂了，我自己写也就那样吧，呵呵，反正也写不出来