#P61
n=int(input("請輸入正整數"))
list1=[]
for i in range(1,n):
    if n%i==0:
        list1.append(i)
#print(list1)
s=0
for i in range(len(list1)):
    s+=list1[i]
if n==s:
    print("perfect")
elif n>s:
    print("deficient")
else:
    print("abundant")