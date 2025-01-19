'''
direction=[[-1,0],[1,0],[0,1],[0,-1]] #首先先定义移动方向
#应该需要两个矩阵，一个标记来没来过，一个标记具体数值。
def num_count(n,m,matrix):
    location_matrix=[[0]*m for _ in range(n)] #这是一个表示位置访问的矩阵
    max_score=float('-inf') #初始化最大为负无穷
    best_path=[] #储存路径坐标

    def dfs(now_x,now_y,current_score,path):
        nonlocal max_score,best_path
        if not (0<=now_x<n and 0<=now_y<m) or location_matrix[now_x][now_y]==1:
            return
        if now_x==n-1 and now_y==m-1: #表示已经走完了所有格子
            current_score+=matrix[now_x][now_y]
            if current_score>max_score:
                max_score=current_score
                best_path=path+[(now_x,now_y)]

            return

        location_matrix[now_x][now_y]=1
        current_score+=matrix[now_x][now_y] #更新当前路径总分

        for i in range(4):
            dfs(now_x+direction[i][0],now_y+direction[i][1],current_score,path + [(now_x,now_y)])

        location_matrix[now_x][now_y]=0#回溯

    dfs(0,0,0,[])
    return max_score,best_path

n,m=map(int,input().split())
matrix=[]
for _ in range(n):
    matrix[0:m-1]=input().split()
max_score,best_path=num_count(n,m,matrix)
for nums in best_path:
    print(nums)
'''
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # 定义移动方向,每一个子列表代表一个可能的移动方向

def num_count(n, m, matrix):
    location_matrix = [[0] * m for _ in range(n)]  # 表示位置访问的矩阵
    max_score = float('-inf')  # 初始化最大为负无穷，来找最大值。
    best_path = []  # 储存路径坐标

    def dfs(now_x, now_y, current_score, path):
        nonlocal max_score, best_path
        if not (0 <= now_x < n and 0 <= now_y < m) or location_matrix[now_x][now_y] == 1:
            return #如果不在范围内或者已经被访问，返回，退出当前递归分支
        if now_x == n - 1 and now_y == m - 1:  # 表示已经走完了所有格子
            current_score += matrix[now_x][now_y]
            if current_score > max_score:
                max_score = current_score
                best_path = path + [(now_x, now_y)]
            return

        location_matrix[now_x][now_y] = 1
        current_score += matrix[now_x][now_y]  # 更新当前路径总分

        for i in range(4):
            dfs(now_x + direction[i][0], now_y + direction[i][1], current_score, path + [(now_x, now_y)])

        location_matrix[now_x][now_y] = 0  # 回溯

    dfs(0, 0, 0, [])
    return max_score, best_path

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

max_score, best_path = num_count(n, m, matrix)
for nums in best_path:
    print(nums[0]+1,nums[1]+1)







