#深度优先搜索，来做，未来问一下ai我该怎么做
def generate_permutation(n):
    nums=list(range(1,n+1))#先获得一个装满所有需要排列的数字的列表
    def dfs(path,choices):
        if len(path)==n:
            print(' '.join(map(str,path)))
            return
        for i in range(len(choices)):
            num=choices[i]
            path.append(num)
            new_choices=choices[:i]+choices[i+1:]
            dfs(path,new_choices)
            path.pop()
    dfs([],nums)

n=int(input())
generate_permutation(n)

