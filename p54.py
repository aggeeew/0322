km=float(input("請輸入路程公里數(km)"))
total=75
if km>1.5:
    if km-1.5<0.25:#如果超過1.5 但沒超過1.5+0.25
        total+=5
    else:
        if (km-1.5)%0.25==0:#超過1.5 增加的數是0.25的倍數
            up=(km-1.5)/0.25*5
            total+=up
        else:
            up=(km-1.5)//0.25*5#超過1.5 增加的數不是0.25的倍數
            total=total+up+5
print("所需車資為:",round(total))