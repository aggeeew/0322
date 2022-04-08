str1="紅豆生南國，春來發幾枝?願君多采擷，此物最相思。"
str2="春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。"
b=set(str1)
a=set(str2)

ans=a & b
ans.remove("，")
ans.remove("。")
print(ans)