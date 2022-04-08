#P26
while True:
    str1=input("檢測的字串(end結束)")
    list1=list(str1)
    #print(list1)
    if str1=="end":
        print("檢測結束")
        break
    else:
        str2=str(input("檢測的單一字元"))
        a=list1.count(str2)
        print("字元{0}出現次數為:{1}".format(str2,a))