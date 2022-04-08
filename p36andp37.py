#p36
num=int(input("輸入T筆資料1<=T<=20"))
list1=[]
list2=[]
for i in range(num):
    for t in range(4):
        a=int(input())
        list1.append(a)
    list2.append(list1)
    list1=[]
    
for i in range(num):
    if list2[i][3]-list2[i][2]==list2[i][2]-list2[i][1] and list2[i][1]-list2[i][0]==list2[i][2]-list2[i][1]:
        for j in range(4):
            a=list2[i][j]
            print(a,end=" ")
        b=list2[i][3]-list2[i][2]
        print(a+b)
        print("此為等差數列")

    elif list2[i][3]/list2[i][2]==list2[i][2]/list2[i][1] and list2[i][1]/list2[i][0]==list2[i][2]/list2[i][1]:
        for t in range(4):
            a=list2[i][t]
            print(a,end=" ")
        b=list2[i][3]/list2[i][2]
        print(int(a*b))
        print("此為等比數列")


#p37
n=int(input("整數n"))
print("數列:",n,end=" ")
while n!=1:
    if n%2==1:
        n=3*n+1
        print("%d"%n,end=" ")
    else:
        n=n/2
        print("%d"%n,end=" ")
