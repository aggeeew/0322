"""
str=input().split(" ")
a=set(str[0])
b=set(str[1])

c=a & b
c.remove("，")
c.remove("。")
c.remove("？")
print(c)
"""
str=input()
list1=list(str)
a1=[]
for i in list1:
    a=list1.count(i)
    if a>1:
        a1.append(i)
result=set(a1)

if "，" in result:
    result.remove("，")
elif "。" in result:
    result.remove("。")
elif "；" in result:
    result.remove("；")
print(result)



