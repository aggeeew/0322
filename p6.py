#p6
str1=list((input("輸入0到9的數字").split(",")))
if len(str1)>7 or len(str1)<1: 
    print("請再輸入一次")
    str1=list(input("輸入0到9的數字"))
else:
    
    int1=list(map(int, str1))
    int1.sort()
    print(int1)

    int2=int1.copy()
    int2.reverse()
    print(int2)
    list1=[]
    c=0
    for i in range(len(int1)):
        int2val=int2[i]
        int1val=int1[i]
        if int2val>=int1val:
            c=int2val-int1val
        else:
            c=10-int1val+int2val
            list1[i-1]-=1
            if list1[i-1]==-1:
                list1[i-1]=9
                list1[i-2]-=1
        list1.append(c)
    print("最大數列與最小數列差值為",end="")
    for i in range(len(list1)):
        print(list1[i],end="")
    
