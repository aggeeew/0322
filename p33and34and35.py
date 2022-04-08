#p33
list1=[]
list2=[]
ch=int(input("國文"))
list1.append(ch)
list2.append("國文")

en=int(input("英文"))
list1.append(en)
list2.append("英文")

cal=int(input("微積分"))
list1.append(cal)
list2.append("微積分")

py=int(input("體育"))
list1.append(py)
list2.append("體育")

pro=int(input("程式設計"))
list1.append(pro)
list2.append("程式設計")

sum=(ch+en+cal+py+pro)/5

max=max(list1)
maxindex=list1.index(max)
min=min(list1)
minindex=list1.index(min)
print("平均分數%.2f"%sum)

print("最高分科目:{0}{1}分".format(list2[maxindex],max))
print("最低分科目:{0}{1}分".format(list2[minindex],min))

#P34
a=int(input("輸入一個正整數"))
if a%2==0 and a%11==0:
    if a%5!=0 and a%7!=0:
        print(a,"為新公倍數?:yes")
else:
    print(a,"為新公倍數?:no")

#p35
sa=str(input("sA"))
sb=str(input("sB"))
if sa in sb:
    print("子字串判斷為:yes")
else:
    print("子字串判斷為:no")