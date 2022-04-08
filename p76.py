password=list(map(int,input("請輸入傳送密碼(6位數)")))
while len(password)<6:
    print("請重新輸入")
    password=list(map(int,input("請輸入傳送密碼(6位數)")))
str1=''

for j in password:
    for i in range(1,10):
    
        if (i*4)%7==j:
            str1+=str(i) 
            break 
print("解密後的密碼:",str1)

