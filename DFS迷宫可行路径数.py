#1为墙壁，0为道路，起点在最左上角，终点在最右下角，迷宫大小为n*m
direction=[(-1,0),(0,-1),(1,0),(0,1)]
#首先初始化行走规则，以便在下面进行移动
def dfs(maze,x,y):#对于这个函数，接受一个矩阵，一个坐标
    global cnt #这里一般是我们要的结果，声明全局变量，这里要的是路径数量
    for i in range(4):
        new_x,new_y=x+direction[i][0],y+direction[i][1]#移动
        if maze[new_x][new_y]=='e': #原地修改处理走迷宫问题
            cnt+=1
            continue
            #通过将终点标记为e，我们到了e就给全局变量加个1就好
        if maze[new_x][new_y]==0:
            maze[x][y]=1#标记刚刚的点为已经访问过
            dfs(maze,new_x,new_y)#继续走
            maze[x][y]=0#然后回溯

    return

n,m=map(int,input().split())
maze=[]
maze.append([-1 for x in range(m+2)])
for _ in range(n):
    maze.append([-1]+[int(_) for _ in input().split()]+[-1])
maze.append([-1 for x in range(m+2)])
#上面是在加保护圈，防止越界,而且此时索引就等于坐标，非常方便
maze[1][1]='s'
maze[n][m]='e'
cnt=0
dfs(maze,1,1)
print(cnt)
#最简单的思路，还是比较清晰，我们多看点例题吧。
