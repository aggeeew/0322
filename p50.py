#p50
fullstudent=set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
en=set(['John','Mary','Fiona','Claire','Ben','Bill'])
math=set(['Mary','Fiona','Claire','Eva','Ben'])
ans1=en & math #交集
ans2=fullstudent - math #差集
ans3=en & ans2
print("英文與數學都及格",ans1)
print("數學不及格",ans2)
print("英文及格且數學不及格",ans3)




