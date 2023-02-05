# while 迴圈
n=1
# while True:
#     print(n)
#     n+=1 # 無限迴圈 (Ctrl + C 中斷)
while n<=3:
    print(n)
    n+=1 # 無限迴圈 (Ctrl + C 中斷)
# 1+2+3+...+10
n=1
sum=0 # 紀錄累加的結果
while n<=10:
    sum=sum+n
    n+=1
print(sum)
# for 迴圈
for x in [3,5,1]:
    print(x)
for x in "Hello":
    print(x)
for x in range(5):
    print(x)
for x in range(5,10):
    print(x)
sum=0
for x in range(1,11): # 1+2+3+...+10
    sum=sum+x
print(sum)