n=int(input())
if n>=2 and n<=10:
    list1=[]
    list2=[]
    for i in range(n):
        
        k=int(input())
        if k>=1 and k<=1000:

            list1.append(k)

            
    for i in range(len(list1)):
        if list1[i]%9==0 or list1[i]%11==0:
            list2.append(list1[i])
for i in range(len(list2)):
    a=list2[i]
    b=list1.index(a)
    print("第",b+1,"個點",a)