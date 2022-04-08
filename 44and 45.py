#p44
t=int(input("1<=T<=10"))
list1=[]
if t>=1 and t<=10:
    for i in range(t):
        num=int(input())
        list1.append(num)
max=max(list1)
print(max)
        
#45
m=int(input("輸入月"))
d=int(input("輸入日"))
s=(m*2+d)%3
if s==0:
    print("普通")
elif s==1:
    print("吉")
elif s==2:
    print("大吉")