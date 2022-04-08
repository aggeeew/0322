a=int(input("輸入a係數"))
b=int(input("輸入b係數"))
c=int(input("輸入c係數"))

d=b**2-4*a*c
dsquare=d**(1/2)
if d>0:
    ans1=(-b+dsquare)/(2*a)
    ans2=(-b-dsquare)/(2*a)
    print(round(ans1))
    print(round(ans2))
elif d==0:
    ans1=(-b+dsquare)/(2*a)
    print(round(ans1))
else:
    print(0)