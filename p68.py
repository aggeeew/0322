#p68
first=input("請輸入第一組數字")
second=input("請輸入第二組數字")
list1=list(first)
list2=list(second)
a=0
b=0
if len(list1)>=2 and len(list1)<=6:
    for i in range(len(list1)):
        if list1[i]==list2[i]:
            a+=1
        elif list1[i] in list2:
            b+=1
    if a==len(list1) and b==0:
        print("{0}A{1}B".format(a,b),"全對")
    else:
        print("{0}A{1}B".format(a,b),"加油")