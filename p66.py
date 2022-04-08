#p66
str1=str(input("請輸入string_a:"))
str2=str(input("請輸入string_b:"))
set1=set(str1)
set2=set(str2)
ans=set1 & set2
list1=list(ans)
list1.sort()
if len(list1)==0:
    print("N")
else:
    for i in range(len(list1)):
        print(list1[i],end="")