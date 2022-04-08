#p17
firsta,firstb=map(int,(input("第一個矩陣").split(" ")))
list1=[]
list2=[]
for i in range(firsta):
    firstrow=list(map(int,input().split(" ")))
    list1.append(firstrow)

seca,secb=map(int,(input("第二個矩陣").split(" ")))

for i in range(seca):
    secrow=list(map(int,input().split(" ")))
    list2.append(secrow)

#print(list2)
#print(list1)


list4=[]
if firstb!=secb or firsta!=seca:
    print("兩個矩陣無法相加")
else:
    for i in range(firsta):
        for t in range(firstb):
            b=list1[i][t]+list2[i][t]
            
            list4.append(b)
    print(list4)
    for i in range(firsta):
        for j in range(firstb):
            a=list4[0]
            print(a,end=" ")
            list4.remove(a)
        print()



#p18
poker=input("輸入5張牌").split(" ")
#print(poker)
list2=[]
for i in poker:
    if i=="A":
        list2.append(int(1))
    elif i=="J":
        list2.append(int(11))
    elif i=="Q":
        list2.append(int(12))
    elif i=="K":
        list2.append(int(13))
    else:
        list2.append(int(i))
#print(list2)
sum=0
for t in list2:
    sum+=t
print(sum)

#p19
num1=int(input("測試的資料量"))
list1=[]
for i in range(num1):
    bloodtype=list(map(str,input("輸入血型").split(" ")))
    list1.append(bloodtype)
    #print(list1)
for i in range(num1):
    if list1[i][0]=="O":
        if list1[i][1]=="o":
            if list1[i][2]=="o":
                print("yes")
            else:
                print("impossible")
        elif list1[i][1]=="A":
            if list1[i][2]=="A" or list1[i][2]=="O":
                print("yes")
            else:
                print("impossible")
        elif list1[i][1]=="B":
            if list1[i][2]=="B" or list1[i][2]=="O":
                print("yes")
            else:
                print("impossible")
        elif list1[i][1]=="AB":
            if list1[i][2]=="A" or list1[i][2]=="B":
                print("yes")
            else:
                print("impossible")
    elif list1[i][0]=="A":
        if list1[i][1]=="A":
            if list1[i][2]=="A" or list1[i][2]=="O":
                print("yes")
            else:
                print("impossible")
        elif list1[i][1]=="B":
            print("yes")
        elif list1[i][1]=="AB":
            if list1[i][2]=="A" or list1[i][2]=="B" or list1[i][2]=="AB":
                print("yes")
            else:
                print("impossible")
    elif list1[i][0]=="B":
        if list1[i][1]=="B":
            if list1[i][2]=="B" or list1[i][2]=="O":
                print("yes")
            else:
                print("impossible")
        elif list1[i][1]=="AB":
            if list1[i][2]=="A" or list1[i][2]=="B" or list1[i][2]=="AB":
                print("yes")
            else:
                print("impossible")
    elif list1[i][0]=="AB":
        if list1[i][1]=="AB":
            if list1[i][2]=="B" or list1[i][2]=="A" or list1[i][2]=="AB":
                print("yes")
            else:
                print("impossible")


#p20
num1=int(input("組數為"))
list1=[]
tick1=[]
tick2=[]
for i in range(num1):
    tic=list(map(int,input("第%s組"%(i+1)).split(" ")))
    #print(tic)
    list1.extend(tic)
    #print(list1)
for j in range(len(list1)):
    if (j+1)%2==1:
        a=list1[j]*250
        tick1.append(a)
    else:
        b=list1[j]*175
        tick2.append(b)
#print(tick1)
#print(tick2)

for t in range(num1):
    sum=tick1[t]+tick2[t]
    print("第%s組應收費用為"%(t+1),sum)



#P21
list1=[[123,"Tom","DTGD"],[456,"Cat","CSIE"],[789,"Nana","ASIE"],[321,"Lim","DBA"],[654,"won","FDD"]]
number=int(input("輸入查詢學號為"))

listnum=[]
listname=[]
listc=[]
for i in range(len(list1)):
    listnum.append(list1[i][0])
    listname.append(list1[i][1])
    listc.append(list1[i][2])
a=listnum.index(number)
print(a)
print("學生資料",number,listname[a],listc[a])



#p23
list1=[]
while True:
    n=int(input("輸入值n為"))
    if n<=100 and n>0:
        ans=(1/3)*(n**3)
        list1.append(round(ans,1))
    elif n==-1:
            break
for i in range(len(list1)):
    print(list1[i])


#p24
array1=int(input("請輸入陣列大小"))
list1=[]
list2=[]
for i in range(array1):
    a=list(map(int,input().split(" ")))
    list1.extend(a)
    list2.append(a)
#print(list1)
#print(list2)
sum=0
list3=[]
for i in range(array1):
    a=max(list1)
    #print(a)
    sum+=a
    for t in range(array1):  
        for j in range(array1):
        
            if a==list2[t][j]:
                b=(t+1,j+1)
                #print(b)
                list3.append(b)
    list1.remove(a)
#print(sum)
#print(list3)
print("最大值為%s"%sum)
print("位置為{0},{1},{2}".format(list3[0],list3[1],list3[2]))
"""
print("位置為",end="")
for i in range(len(list3)):
    print(list3[i],end="")
"""

