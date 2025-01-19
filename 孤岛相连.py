
import heapq
def dijkstra(x1,y1):
    queue=[]
    vis=[[False]*m for _ in range(n)]
    #首先定义优先队列和已访问标记
    heapq.heappush(queue,(0,x1,y1))
    while queue:
        step,x,y = heapq.heappop(queue)
        if vis[x][y]:
            continue
        vis[x][y]=True
        if matrix[x][y]==1 and step!=0:
            return step
        for dx,dy in direction:
            if 0<=x+dx<n and 0<=y+dy<m and not vis[x+dx][y+dy]:
                heapq.heappush(queue,(step+1-matrix[x+dx][y+dy],x+dx,y+dy))
                    #这个计算，如果新位置是1则步数不变，如果新位置是0则步数加1，比较巧妙
n=int(input())
matrix=[list(map(int,input())) for _ in range(n)]
#首先读取地图
m=len(matrix[0])#获得列数
direction=[(1,0),(-1,0),(0,1),(0,-1)]
#下面开始找起点
for i in range(n):
    for j in range(m):
        if matrix[i][j]==1:
            x1,y1=i,j

print(dijkstra(x1,y1))

