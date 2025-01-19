#这个我自己也比较有思路，就是建一个矩阵，然后在里面填写好数字，下面就判断覆盖面积就可以了，
# 我们只对于有数字的点周围可能被波及到的地方进行测算，可以稍微节省一下时间。
matrix=[[0 for _ in range(1025)] for _ in range(1025)]
k=int(input())
n=int(input())
for _ in range(n):
    x,y,m=map(int,input().split())
    for i in range(max(0,x-k),min(x+k+1,1025)):
        for j in range(max(0,y-k),min(y+k+1,1025)):#在每一个可能安装的地方都计数，会自然加总
            matrix[i][j]+=m
#关键是个数不太好算，因为需要的是最大值最多影响的地方，所以找到一次最大值都要重置计数
max_num=0
f=0
for i in range(1025):
    for j in range(1025):
        if matrix[i][j]>max_num:
            max_num=matrix[i][j]
            f=1
        elif matrix[i][j]==max_num:
            f+=1
print(f,max_num)

#到这里我们的矩阵就填充完毕了，下面我们搞清楚可能安装的范围，在这个范围内遍历每一个，求最大的覆盖
#甚至有可能是集合求交集？

