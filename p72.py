n=int(input("請輸入n"))
k=int(input("請輸入k"))
total=0
if k>1:
    while n>1:
        total+=n
        n=n//k
        if n==1:
            total+=n


print("Peter可以抽{0}支紙菸".format(total))