n=int(input())
activities=[]
ac=0
for _ in range(n):
    m,n=map(int,input().split())
    activities.append((m,n))

activities=sorted(activities,key=lambda x: x[1])
current_time=-1
for activity in activities:
    start,end=activity
    if start>current_time:
        ac+=1
        current_time=end
print(ac)

