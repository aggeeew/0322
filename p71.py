decimal=int(input("請輸入十進位的正整數"))
list1=[]
if decimal<3:
    print("{0}的三進位為{1}".format(decimal,decimal))
else:
    print("{0}的三進位為".format(decimal),end="")
    while decimal>1:
        b=decimal%3
        decimal=decimal//3


        list1.append(b)

 
    list1.append(decimal)
    
    for i in range(len(list1)-1,-1,-1):
        print(list1[i],end="")