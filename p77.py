
with open('data.txt','r') as f:
    content=f.readlines()


list1=[]
list2=[]
for i in content:
  
    a=i.split(", ")

    list1.append(a[0])

    list2.append(a[1])



intlist1=list(map(int,list1))
intlist2=list(map(int,list2))

max1=max(intlist1)
min1=min(intlist1)
s1=0
for i in intlist1:
    s1+=i
aveger1=s1/len(intlist1)
print("血壓平均:",round(aveger1,2))
print("血壓最大值:",max1)
print("血壓最小值",min1)
print()
max2=max(intlist2)
min2=min(intlist2)
s2=0
for i in intlist2:
    s2+=i
aveger2=s2/len(intlist2)
print("心跳平均:",round(aveger2,2))
print("心跳最大值:",max2)
print("心跳最小值",min2)