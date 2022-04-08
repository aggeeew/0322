n=int(input("輸入n值"))
dic={}
for i in range(n):
    name=input("請輸入姓名")
    email=input("請輸入電子郵件")
    dic[name]=email
name1=str(input("請輸入要查詢電子郵件的姓名"))
print("{0}電子郵件帳號為{1}".format(name1,dic.get(name1)))#get 取值 傳入要尋找的鍵(Key)名稱，它會回傳其值(Value)