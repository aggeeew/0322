#p56
num=int(input("請輸入一個正整數"))
s=1
if num<=10 and num>0:
    for i in range(1,num+1):
        for j in range(i):
            print(s,end=" ")
            s+=i
        print()
        s=i+1

        