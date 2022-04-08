#p2
from unittest import result


degree=int(input("輸入度數"))
if degree<=120:
    print("Summer months:%.2f" %(degree*2.10))
    print("Non-Summer months:%.2f" %(degree*2.10))
elif degree>120 and degree<=330:
    print("Summer months:%.2f" %(degree*3.02))
    print("Non-Summer months:%.2f" %(degree*2.68))
elif degree>330 and degree<=500:
    print("Summer months:%.2f" %(degree*4.39))
    print("Non-Summer months:%.2f" %(degree*3.61))
elif degree>500 and degree<=700:
    print("Summer months:%.2f" %(degree*4.97))
    print("Non-Summer months:%.2f" %(degree*4.01))
else:
    print("Summer months:%.2f" %(degree*5.63))
    print("Non-Summer months:%.2f" %(degree*4.50))

#p3
year=int(input("輸入西元年"))
if (year-2010)%12==0 :
    print("tiger")
elif (year-2010)%12==1 or (year-2010)%12==-11:
    print("rabbit")
elif (year-2010)%12==2 or (year-2010)%12==-10:
    print("dragon")
elif (year-2010)%12==3 or (year-2010)%12==-9:
    print("snake")
elif (year-2010)%12==4 or (year-2010)%12==-8:
    print("horsc")
elif (year-2010)%12==5 or (year-2010)%12==-7:
    print("sheep")
elif (year-2010)%12==6 or (year-2010)%12==-6:
    print("monkey")
elif (year-2010)%12==7 or (year-2010)%12==-5:
    print("roostcr")
elif (year-2010)%12==8 or (year-2010)%12==-4:
    print("dog")
elif (year-2010)%12==9 or (year-2010)%12==-3:
    print("pig")
elif (year-2010)%12==10 or (year-2010)%12==-2:
    print("rat")
else:
    print("ox")

#p4
x=int(input("X軸座標"))
y=int(input("y軸座標"))

if x>0 and y>0:
    print("該點位於第一象限，離原點距離為根號",(x**2+y**2))
elif x<0 and y>0:
    print("該點位於第二象限，離原點距離為根號",(x**2+y**2))
elif x<0 and y<0:
    print("該點位於第三象限，離原點距離為根號",(x**2+y**2))
elif x>0 and y<0:
    print("該點位於第四象限，離原點距離為根號",(x**2+y**2))
else:
    if x==0 and y==0:
        print("該點位於原點")
    else:
        if x==0 and y>0:
            print("該點位於上半平面y軸上，離原點距離為根號",y**2)
        elif x==0 and y<0:
            print("該點位於下半平面y軸上，離原點距離為根號",y**2)
        elif x>0 and y==0:
            print("該點位於右半平面x軸上，離原點距離為根號",x**2)
        else:
            print("該點位於左半平面x軸上，離原點距離為根號",x**2)

#p5
m=int(input("請輸入階乘值"))
i=1
s=1
while s<=m:
    s=s*i
    i+=1
print("超過M為%s的最小階乘N值為:" %(m),i-1)




#p7

money,time=map(int,input("輸入月租費型式(186,386,586,986)及通話時間為").split(","))
if money==186:
    if time*0.09>186:
        print("通話費為:",round(time*0.09*0.8))
    else:
        print("通話費為:",round(time*0.09*0.9))
elif money==386:
    if time*0.08>386:
        print("通話費為:",round(time*0.08*0.7))
    else:
        print("通話費為:",round(time*0.08*0.8))
elif money==586:
    if time*0.07>586:
        print("通話費為:",round(time*0.07*0.6))
    else:
        print("通話費為:",round(time*0.07*0.7))
elif money==986:
    if time*0.06>986:
        print("通話費為:",round(time*0.06*0.5))
    else:
        print("通話費為:",round(time*0.06*0.6))

#p8
integer=int(input("輸入第一行正整數"))
list1=list(map(int,input("第二行中數列中的數字為").split(" ")))
list2=set(list1) #set不會重複
list3=[] #放list1 item 次數
list4=[]
if len(list1)==len(list2):
    print("每個數字剛好出現1次")
else:
    for item in list1:
        list3.append(list1.count(item))
    
    maxval=max(list3)
    indexval=list3.index(maxval)

    print("最大出現次數的數字為",list1[indexval])
    print("出現次數為",maxval)


#p9
str1=str(input("輸入S1為"))
str2=str(input("輸入S2為"))
if str1 in str2:
    print("yes")
else:
    print("no")            


