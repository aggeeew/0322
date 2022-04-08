list1=[]
while True:
    a=str(input("請輸入事項(若已無事項，請輸入end)"))
    if a=="end":
        break
    else:
        list1.append(a)

for i in range(len(list1)):
    print("{0}. {1}".format(i+1,list1[i]))