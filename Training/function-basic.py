# 定義函式
def multiply(n1,n2):
    print(n1*n2)
    return n1*n2
# 呼叫函式
value=multiply(3,4)+multiply(10,5)
print(value)

# 程式的包裝
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)

value=int(input("輸入最大數: "))
calculate(value)