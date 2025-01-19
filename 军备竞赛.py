#我就这样美美逃避苦难，这个有意思，让我厘清一下思路。我们的贪心策略就是，买一件卖一件
'''
p=int(input())
list_for_equipment=list(map(int,input().split()))
list_for_equipment=sorted(list_for_equipment)
mine=0
enemies=0
while list_for_equipment:

        if p >= list_for_equipment[0]:
            p-=list_for_equipment[0]
            mine+=1
            list_for_equipment.remove(list_for_equipment[0])
        if mine<=enemies:
            break

        elif len(list_for_equipment)>1:
                p+=max(list_for_equipment)
                list_for_equipment.remove(max(list_for_equipment))
                enemies+=1
                p-=min(list_for_equipment)
                list_for_equipment.remove(min(list_for_equipment))
                mine+=1
        else:
            break
'''
#我操cs,你再不给我数据我把你杀了。我现在大概知道为什么了，因为买进会更加优先，应该是卖出一个·1最大的回来看能买多少，直到不能继续买了
#我决定参考一下答案的思路，我的毕竟比较复杂了。


#可以建一个布尔数组，然后表示现在这个图纸有没有被购买还有卖出，等到所有都被处理过之后，我们就退出
# ，来计算他们的差值
#但好像也不用布尔数，我们直接从列表中删除就可以，最后列表长度为0我们就结算就可以.
p=int(input())
list_for_equipment=list(map(int,input().split()))
list_for_equipment=sorted(list_for_equipment)
mine=0
lf=0
rt=len(list_for_equipment)-1
while lf<=rt:#分成了左边和右边，因为是两个方向分别看，我们就把循环到最大最小两人相遇为止。
    #下面先把买得起的全部买完
    if list_for_equipment[lf]<=p:
        mine+=1
        p-=list_for_equipment[lf]
        lf+=1
    else:
        if rt==lf:
            break
        p+=list_for_equipment[rt]
        mine-=1
        if mine<0:
            mine=0
            break
        rt-=1
print(mine)
#求不要再用cs了，补药啊啊啊啊啊！