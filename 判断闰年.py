year=int(input())
if year<0 or year>3000 :
    print('请输入正确年份')
elif  (year%4==0 and year%100!=0 and year%3200!=0) or year%400==0:
    print("Y")
else:
    print("N")
#我要笑死了问题竟然真的出现在3200年，我有又不到那一天，我知道这些有什么用