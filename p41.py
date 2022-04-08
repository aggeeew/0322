#p41
t=int(input("搭了幾次電梯"))
list1=[]
sum=0
while True:
    if t>=1 and t<=10:
        for i in range(t):
            stair=int(input("到第幾層"))
            
            if stair==1:
                print("輸入錯誤")
                stair=int(input("到第幾層"))
                list1.append(stair)
            else:
                list1.append(stair)
                
        
            
              
            
        for i in range(len(list1)-1):
            
            if list1[i+1]>list1[i]:
                up=list1[i+1]-list1[i]
                total=up*20
                sum+=total
            elif list1[i]>list1[i+1]:
                down=list1[i]-list1[i+1]
                total=down*10
                sum+=total
        
        for i in range(t-1):
            if list1[i]==list1[i+1]:
                print("輸入錯誤")
                break
            else:    
            
                one=list1[0]-1
                sum=sum+one*20
                print(sum,"元")
                break
        break

        
    else:
        print("超出範圍")
        t=int(input("搭了幾次電梯"))