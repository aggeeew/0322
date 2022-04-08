list1=[[123,456,9000],[456,789,5000],[789,888,6000],[336,558,10000],[775,666,12000],[566,221,7000]]
num=int(input("輸入查詢組數N為:"))
list3=[]
list4=[]
for i in range(num):
    list2=list(map(int,input().split(" ")))
    list3.append(list2[0])
    list4.append(list2[1])


for i in range(len(list1)):
    for t in list3:
        n=list3.index(t)
        if list1[i][0]==t:
            
            if list4[n]==list1[i][1]:
                print(list1[i][2])
                
                break
            else:
                print("crror")
         
                break
        
        elif list1[i][0]!=t and list4[n]==list1[i][1]:
            print("crror")
          
            break
        




