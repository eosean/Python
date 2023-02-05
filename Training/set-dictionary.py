# 集合的運算
s1={3,4,5}
print(3 in s1) # 3 是否在集合中: True
print(10 in s1) # 10 是否在集合中: False
print(10 not in s1) # 10 是否不在集合中: True
s2={4,5,6,7}
s3=s1&s2 # 交集: 取兩個集合中 相同的資料
print(s3)
s3=s1|s2 # 聯集: 取兩個集合中所有資料，但不重複
print(s3)
s3=s1-s2 # 差集: 從 s1 中 減去和 s2 重疊部分
print(s3)
s3=s1^s2 # 反交集: 取兩個集合中 不重疊部分
print(s3)
s=set("Helloe") # set(字串)，不會依照順序
print(s)
print("e" in s) # e 是否在字串集合中
# 字典的運算
dic={"apple":"蘋果","bug":"臭蟲"}
print(dic["apple"])
dic["apple"]="小蘋果" # 替換值
print(dic["apple"])
print("apple" in dic) # 判斷key是否存在
del dic["apple"] # 刪除字典中的鍵值對(key-value pair)
print(dic)
dic={x:x*2 for x in [3,4,5]} # 從列表的資料產生字典
print(dic)