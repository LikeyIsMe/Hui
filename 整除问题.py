#还是一样的，先多行输入搞清楚，他是每一行都要执行的
n=int(input())

result=[]
for _ in range(n):
    total_num=0
    m,l=map(int,input().split())
    '''
    while m%l!=0:
        m+=1
        total_num+=1'''

    if m % l != 0:
            increment = l - (m % l)
            total_num = increment
    else:
            total_num = 0

            result.append(total_num)
for number in result:
    print(number)
#用了快一个小时，思路很简单，十分钟就开始会写了，但是因为循环写不对卡了很久，其实这道题非常简单。好聪明，ai提供的是直接算不要一次一次加了，太牛了