#首先，无论如何，单个字符就是长度为1的回文字符串
s=list(map(int,input().split()))
ans=1
s_x,s_y=0,0 #这个是最长回文字符串的起点和终点，初始化为0
n=len(s)
dp=[[False]*n for _ in range(n)] #布尔数组判断dp[i][j]，表示s[i:j+1]是否为回文字符串
#在这里我们从终点开始遍历
for j in range(n):
    for i in range(j,-1,-1): #从j到0逆序遍历
        if j-i >=2: #当这个区间切片获得了三个以上的元素时
            dp[i][j]=dp[i+1][j-1] and s[i]==s[j] #里面包的东西是不是，以及两边一不一样
        else:
            dp[i][j]=s[i]==s[j]
        if dp[i][j]==True and j-i+1>ans:
            ans=j-i+1
            s_x,s_y=i,j #不断更新最长值以及起点终点
return s[s_x:s_y+1]
#先判断中间是不是回文字符串，然后再判断两边是不是回文


