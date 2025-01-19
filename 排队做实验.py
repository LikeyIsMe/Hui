#我真的笑了，这个又是在干嘛，我就像那种阳痿的丈夫，已经不知道人间的意义在何方了....
#好的，就是一个排序，我们现在要根据数字大小给他们的序号进行排序，加油！
def sort_indices(nums):
    indexed_nums = [(value, index) for index, value in enumerate(nums)]# 创建一个元组列表，包含 (值, 索引)
    sorted_nums = sorted(indexed_nums, key=lambda x: x[0])# 按照值进行排序
    result = [index + 1 for _, index in sorted_nums]# 生成结果列表，包含排序后的索引
    return result
n=int(input())
nums = list(map(int, input().split()))
sorted_ones = sort_indices(nums)
print(' '.join(map(str, sorted_ones)))
nums=sorted(nums)
total=0
a=0
for i in nums:
    total+=a
    a+=i
average=total/n
print(f'{average:.2f}')
#好了终于处理完第一个了，好开心！
#下面处理这个巨搞笑的平均数，我们用循环来做。