time1=input("請輸入時間1(時:分:秒)")
time2=int(input("請輸入時間2(秒)"))
time1_1=time1.split(":")
time2_copy=time2
list1=list(map(int,time1_1))

turntime1=list1[0]*60*60+list1[1]*60+list1[2]

print("時間1({0})格式轉換後為{1}秒".format(time1,turntime1))
a=time2//3600
time2=time2-3600*a
b=time2//60
time2=time2%60
print("時間2({0})={1}:{2}:{3}".format(time2_copy,a,b,time2))
