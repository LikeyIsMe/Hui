'''#思路是输入然后开始检索，可能需要引入字典好像是
original_string_1=input()
original_string_2=input()
trans_string_1=original_string_1.lower()
trans_string_2=original_string_2.lower()

for i,k in range(len(trans_string_1),len(trans_string_2)):
    char1=(trans_string_1[i])
    char2=(trans_string_2[k])
    number_for_1=ord(char1)
    number_for_2=ord(char2)
    if number_for_1>number_for_2:
        print("-1")
    elif number_for_1<number_for_2:
        print("1")
    elif number_for_2==number_for_1:
        print("0")
    '''
# 读取输入
string1 = input().strip()
string2 = input().strip()

# 将字符串转换为小写
string1_lower = string1.lower()
string2_lower = string2.lower()

# 比较字符串
if string1_lower < string2_lower:
    print(-1)
elif string1_lower > string2_lower:
    print(1)
else:
    print(0)
#好吧原来直接就可以比较字母顺序是我孤陋寡闻还想多了，就这样吧，在此我做完作业了。