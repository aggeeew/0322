dic1={"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
fru=str(input("請輸入水果"))

item1=list(dic1.items())
#print(item1)
for a,b in item1:
    if fru==a:
        print("{0}是{1}".format(fru,b))