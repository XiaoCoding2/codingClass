
from sys import (set_int_max_str_digits, getrecursionlimit, setrecursionlimit)
from termcolor import colored
from functools import cache
from time import perf_counter

# Code to test fastest way to get fibonacci numbers
# Cache saves the last result, making the code quicker becuase it doesn't calculate all previous fib numbers
# perf counter mesures time of each function

setrecursionlimit(10_000)
print(getrecursionlimit())

# 1. recursion
@cache
def fibo(a: int) -> int:
    if a==0:
        return 0
    elif a==1:
        return 1
    elif a==2:
        return 1
    return fibo(a-1)+fibo(a-2)
# 2. iterative
@cache
def fibo2(a:int) -> int:
    if a<=1:
        return a
    first_num:int=0
    second_num:int=1
    next_num:int
    for x in range(a -1):
        next_num=first_num+second_num
        first_num,second_num=second_num,next_num
    return next_num

print(fibo2(14))
raise
# Test Function
def test(func, n: int) -> None:
    set_int_max_str_digits(1_000_000)
    start=perf_counter()
    while True:
        try:
            func(30)
            break
        except Exception as e:
            print(colored("ERROR",'red'),end=": ")
            print(e)
            break
    end=perf_counter()
    print(f"Solution{n} exec time: {end-start}")
    func.cache_clear()

def main():
    if __name__=="__main__":
        test(fibo,1)
        print("-"*50) # seperator
        test(fibo2,2)

main()