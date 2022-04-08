a=input("請輸入A的好友").split(" ")
b=input("請輸入B的好友").split(" ")

seta=set(a)
setb=set(b)
#print(seta)
#print(setb)
c=seta & setb
len=len(c)
print(len)