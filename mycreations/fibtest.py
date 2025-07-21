
num1:int=0
num2:int=1
sum1:int
for x in range(2,1001):
    sum1=num1+num2
    num1=num2
    num2=sum1
    print(f"sum={sum1}")

