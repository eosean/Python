# 數字運算
x=3+6
print(x)
x=3-6
print(x)
x=3*6
print(x)
x=3/6 # 小數除法
print(x)
x=3//6 # 整數除法
print(x)
x=7%3 # 除法 取餘數
print(x)
x=2**3 # 次方: 2的3次方
print(x)
x=4**0.5 # 開根號
print(x)
# 字串運算
x='Hello'
x="Hello"
print(x)
x="Hell\"o" # 雙引號前加入\ 使其跳脫
print(x)
x="Hello" "World" # 加號+ 或 空格 都可以串接字串
print(x)
x="Hello\nWorld" # \n 字串換行
print(x)
x='''Hello
World''' # 3個雙引號or單引號 可直接換行
print(x)
x="Hello"*3+"World" # 字串重複3遍 +再接字串
print(x)
# 字串會對內部字元編號(索引),從0開始算起
x="Hello"
print(x[0]) # 字串第0個
print(x[1:4]) # 字串中 1~4 字元
print(x[1:]) # 字串中 1~結束 字元
print(x[:4]) # 字串中 開始~4 字元