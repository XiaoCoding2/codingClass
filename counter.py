
from collections import Counter as C

def ex1():
    data1 = [1, 1, 1, 3, 3, 2, 4, 4, 8]
    counter = C(data1)
    print(counter)
#ex1()
def ex2():
    data = {'cat': 5, 'dogs': 2}
    counter = C(data)
    print(counter)
#ex2()
def ex3():
    data2 = ['a', 'b', 'a']
    counter = C(data2)
    print(counter['a'])
#ex3()
def ex4():
    data3 = ['a', 'b', 'c']
    counter = C(data3)
    data3_ = ['a']
    counter.update(data3_)
    print(counter)
#ex4()
def ex5():
    '''
    1. Instances of the word "is"
    2. Instances of the character i
    3. pull all the words from that sentence that show up exactly twice
    '''

    data4 = "this is a test sentence this is"
    data4_list = data4.split()
    counter = C(data4_list)
    print(counter['is'])
    counter1 = C(data4)
    print(counter1['i'])
    for word, amount in counter.items():
        if amount == 2:
            print(word)
#ex5()
