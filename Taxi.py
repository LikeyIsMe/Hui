#感觉这道题难度也不是特别大啊，先把4的提出来，然后找出3的，再去找1的和他们一个车，
# 最后去找2的，然后多的再找1的一个车，最后结束
import math
n=int(input())
lst_for_groups=list(map(int,input().split()))
Taxi=0
count_for_4=0
count_for_3=0
count_for_2=0
count_for_1=0
for num in lst_for_groups:
    if num==4:
        count_for_4+=1
    elif num==3:
        count_for_3+=1
    elif num==2:
        count_for_2+=1
    elif num==1:
        count_for_1+=1


Taxi+=count_for_4

if count_for_3>=count_for_1:
    Taxi+=count_for_3
    count_for_1=0
elif count_for_1>count_for_3:
    count_for_1=count_for_1-count_for_3
    Taxi+=count_for_3

if count_for_2%2==0:
    Taxi+=count_for_2//2
else:
    Taxi+=(count_for_2-1)//2
    Taxi+=1
    if count_for_1>=2:
        count_for_1-=2
    elif count_for_1==1:
        count_for_1=0

Taxi+=math.ceil(count_for_1/4)
print(Taxi)