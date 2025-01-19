#这道题好像要处理很多东西，好吧，三个周期三线进程，23，28，33，
# 三个周期都有对应的高峰，好像懂了，就是那种
# 🆗，我们的贪心思路就是四个数字，分别生成等差数列，然后再遍历寻找交叉项，最后算出来的再与输入的
# 天数相减就可以了。实质上是寻找等差数列的交叉项，我们要不先预计算把0为首项，公差三个分别先算出来
'''
all_miracles=[]
while True:
    try:
        d,e,p,k=map(int,input().split())
        if d==e==p==k==-1:
            break
        sequence_1=[d+i*23 for i in range(1,1000)]
        sequence_2=[e+i*28 for i in range(1,1000)]
        sequence_3=[p+i*33 for i in range(1,1000)]
        set_1=set(sequence_1)

        set_2=set(sequence_2)
        set_3=set(sequence_3)
        common=set_1&set_2&set_3
        common=list(common)
        matrix=[i-k for i in common]
        all_miracles.append(matrix)
    except ValueError:
        break
for i,num in enumerate(all_miracles):
    for j in all_miracles[i]:
        print(f'Case {i}: the next triple peak occurs in {j} days')
#我服了这个世界，要害我为什么要用计算概论，我是什么很贱的人嘛，索性现在先不看这题了，呵呵，我先去打军备竞赛了！'''
#自己的太复杂了，学习一下这位朋友的思路
n = 0
while True:
    a, b, c, d = map(int, input().split())
    n += 1
    if a + b + c + d >= 0:
        found = False
        for i in range(1, 21253):
            if (i - a) % 23 == 0 and (i - b) % 28 == 0 and (i - c) % 33 == 0:
                if i - d >= 0:
                    print(f"Case {n}: the next triple peak occurs in {i - d} days.")
                else:
                    print(f"Case {n}: the next triple peak occurs in {i - d + 21252} days.")
                found = True
                break
        if not found:
            print(f"Case {n}: No valid solution found within the range.")
    else:
        break



