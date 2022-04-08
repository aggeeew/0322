#p58
list1=[]
for i in range(1,11):
    num=int(input("請輸入第%s個數字"%i))
    list1.append(num)

list2=[]
list3=[]
for i in range(3):
    max1=max(list1)
    min1=min(list1)
    list2.append(max1)
    list3.append(min1)
    list1.remove(max1)
    list1.remove(min1)
print("最大的3個數字為:{0},{1},{2}".format(list2[0],list2[1],list2[2]))
print("最小的3個數字為:{0},{1},{2}".format(list3[0],list3[1],list3[2]))