# 載入內建的 sys 模組並取得資訊
import sys
print(sys.platform)
print(sys.maxsize)
import sys as system # as 取一個別名 system
print(system.platform)
print(system.maxsize)
# 建立 geometry 模組(geometry.py)，載入使用
sys.path.append("modules") # 在模組的搜尋路徑列表[新增路徑]
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)
# 調整搜尋模組的路徑
print(sys.path) # 印出模組的搜尋路徑列表