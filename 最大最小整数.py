'''#就是一个字符串的一个组合问题
n=int(input())
lst_int=list(map(str,input().split()))
#检查几个数字的最大位，并进行排序
#如果出现相同的，则继续排序，直到排出顺序或者有一个结束
#将最终排序的字符串正组装以及反组装，获得两个整数

for i in lst_int:
    a=int(i[0])
'''
n=int(input())
nums=input().split()
nums_str=[str(num) for num in nums]
sorted_max=sorted(nums_str,key=lambda x:x*6,reverse=True)
max_num=''.join(sorted_max)
sorted_min=sorted(nums_str,key=lambda x:x*6)
min_num=''.join(sorted_min)
#需要考虑第一位为0的情况
if min_num[0]=='0':
    min_num=min_num[1:]
if min_num=='':
    min_num='0'
print(max_num,min_num)
