#p11



month,day=map(int,input("請輸入月及日").split(" "))
if month==1:
    if day>=21:
        print("星座為Aquarius")
    else:
        print("星座為Capricorn")
elif month==2:
    if day>=19:
        print("星座為Pisces")
    else:
        print("星座為Aquarius")
elif month==3:
    if day>=21:
        print("星座為Aries")
    else:
        print("星座為Pisces")
elif month==4:
    if day>=21:
        print("星座為Taurus")
    else:
        print("星座為Aries")
elif month==5:
    if day>=22:
        print("星座為Gemini")
    else:
        print("星座為Taurus")
elif month==6:
    if day>=22:
        print("星座為Cancer")
    else:
        print("星座為Gemini")
elif month==7:
    if day>=23:
        print("星座為Leo")
    else:
        print("星座為Cancer")
elif month==8:
    if day>=24:
        print("星座為Virgo")
    else:
        print("星座為Leo")
elif month==9:
    if day>=24:
        print("星座為Libra")
    else:
        print("星座為Virgo")
elif month==10:
    if day>=24:
        print("星座為Scorpio")
    else:
        print("星座為Libra")
elif month==11:
    if day>=23:
        print("星座為Sagittarius")
    else:
        print("星座為Scorpio")
elif month==12:
    if day>=22:
        print("星座為Capricorn")
    else:
        print("星座為Sagittarius")

#p12
list1=list(map(int,input("輸入一整數序列").split(" ")))
list2=[]
for i in list1:
    list2.append(list1.count(i))
max1=max(list2)
index1=list2.index(max1)#把次數最大的索引值找出來  max1的位置
if max1>len(list1)/2:
    print("過半元素為:",list1[index1])
else:
    print("過半元素為:no")

#p13
a=str(input("輸入一字元"))
list1=list(a)
list2=list(a)
list2.reverse()#反轉list
if list2==list1:
    print("yes")
else:
    print("no")

#p14
str1=str(input("輸入一個字串"))
list1=list(str1)
a=len(list1)
print("there are %s characters" %(a))

#p15
num1=input("輸入一組四位數字")
list1=list(map(int,num1))#把字串改成int list
for i in range(len(list1)):
    list1[i]=(list1[i]+7)%10

#位置1和3交換
tmp1=list1[0]
list1[0]=list1[2]
list1[2]=tmp1

#位置2和4交換
tmp2=list1[1]
list1[1]=list1[3]
list1[3]=tmp2
#print(list1)
print("輸入加密後的數字為{0}{1}{2}{3}".format(list1[0],list1[1],list1[2],list1[3]))

