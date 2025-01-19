n=int(input())
matrix=[]

for _ in range(n):
    matrix.append(list(map(int,input().split())))
#初始化洋葱矩阵，然后开始遍历一层一层
layer_sum=[]
start=1
top,bottom,left,right=0,n-1,0,n-1
while start<=n*n:
    k=0
    for i in range(left,right+1):
        k+=matrix[top][i]
        start+=1
    top+=1

    for i in range(top,bottom+1):
        k+=matrix[i][right]
        start+=1
    right-=1

    if top<=bottom:
        for i in range(right,left-1,-1):
            k+=matrix[bottom][i]
            start+=1
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            k+=matrix[i][left]
            start+=1
        left+=1
    layer_sum.append(k)
print(max(layer_sum))




