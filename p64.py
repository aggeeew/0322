int1=int(input("請輸入第一個要判斷的數字"))
int2=int(input("請輸入第二個要判斷的數字"))

if int1%2==1 and (int1+2)%2==1:
    if int2%2==1 and (int2+2)%2==1:
        print("Y")
    else:
        print("N")
else:
    print("N")
  

