# 有序可變動列表 List
grades=[12,60,15,70,90]
grades[1]=20 # 變更 編號1的參數
grades[1:4]=[] # 連續刪除列表中 編號1~4(不包含4)的資料
grades=grades+[12,33] # 列表串接
print(grades)
length=len(grades) # 取得 列表長度 len(列表資料)
print(length)
# 巢狀列表
data=[[3,4,5],[6,7,8]]
print(data)
data[0][0:2]=[5,5,5]
print(data)
# 有序不可變動列表 Tuple
data=(3,4,5)
data[0]=5 # 錯誤: Tuple的資料不可變動
print(data) 