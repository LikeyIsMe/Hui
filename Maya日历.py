#这大哥到底在说什么，直接被绕晕了......
import re
def haab_to_tzo(num,mouth,year):
    #先把玛雅天转换为总天数，先创建一个字典吧，把对应的数字填写进去。
    haab_days={'pop':0,'no':20,'zip':40,'zotz':60,'tzec':80,'xul':100,'yoxkin':120,'mol':140,'chen':160,'yax':180,'zac':200,'ceh':220,'mac':240,'kankin':260,'muan':280,'pax':300,'koyab':320,'cumhu':340,'uayet':360}
    total_days=num+haab_days[mouth]+year*365
    #下面得到总天数之后，又转化为冬青年纪年，
    year=total_days//260
    total_days=total_days%260
    tzo_days=total_days%13+1

    tzo_month=total_days%20
    tzo_month_trans={0:'imix',1:'ik',2:'akbal',3:'kan',4:'chicchan',5:'cimi',6:'manik',7:'lamat',8:'muluk',9:'ok',10:'chuen',11:'eb',12:'ben',13:'ix',14:'mem',15:'cib',16:'caban',17:'eznab',18:'canac',19:'ahau'}
    tzo_month=tzo_month_trans[tzo_month]
    return tzo_days,tzo_month,year

n=int(input())
matrix=[]
for _ in range(n):
    maya_days = input()
    maya_days = re.findall(r'\d+|[a-zA-Z]+', maya_days)
    clean_maya_days = [token for token in maya_days if token.strip()]

    a=clean_maya_days[0]
    b=clean_maya_days[1]
    c=clean_maya_days[2]
    tzo_days,month,year=haab_to_tzo(int(a),b,int(c))
    matrix.append([tzo_days,month,year])
print(n)
print('\n'.join(' '.join(map(str,sublist)) for sublist in matrix))
#这道题不难，笑死，居然卡在单词拼写错了这件事，没啥吧，学到了正则表达式分割，最后发现原来split就可以分割