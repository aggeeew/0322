#p60
str1=str(input("請輸入一串小寫英文:"))
list1=list(str1)
#print(list1)

for i in range(len(list1)):
    if list1[i]=="a" or list1[i]=="e" or list1[i]=="i" or list1[i]=="o" or list1[i]=="u":
        list1[i]="."
    print(list1[i],end="")