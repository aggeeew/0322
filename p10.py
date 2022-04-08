#p10

n,m=map(int,input("輸入n及m為").split(" "))
list1=[]
list2=[]

for i in range(n):
    a=list(map(int,input("輸入矩陣數值第%s列為"%(i+1)).split(" ")))
    list1.append(a)
print(list1)

for i in range(m):
    for t in range(n):
        list2.append(list1[t][i])

print(list2)

for i in range(m):
    print("輸出矩陣數值第%s列為"%(i+1),end="")
    for t in range(n):
        print(list2[0],end=" ")
        list2.pop(0)
    print()



