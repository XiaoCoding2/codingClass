#Projects

#cut duplicate numbers
list1 = [0,1,2,3,3,2]
list2 = []

def no_dupes():
    for x in list1:
        if x not in list2:
            list2.append(x)
def better1():
    lst = [0,1,2,3,3,2]
    lst2 = []
    [lst2.append(x) for x in lst if x not in lst2]
    return lst2
#no_dupes()
#print(list2)
#print(better1())

#Cut words under 3 letters
word = []

def remove_words(n,string):
    txt = string.split(" ")
    for x in txt:
        l = len(x)
        if l >= n:
            word.append(x)
def better2(l, s):
    word = [x for x in s.split(" ") if len(x) >= l]
    return word
#remove_words(3,"I am a tomato and likes soup.")
#print(word)
#print(better2(3, "I am a tomato and likes soup."))

#Fomula Help
def inputs():
    ask = input("What fomula do you need?: ")
    if ask == 'rectangle':
        ask2 = int(input("Please enter base: "))
        ask3 = int(input("Please enter height: "))
        print(rectangle(ask2, ask3))

    elif ask == 'triangle':
        ask2 = int(input("Please enter base: "))
        ask3 = int(input("Please enter height: "))
        print(triangle(ask2, ask3))
    
    elif ask == 'circle':
        ask4 = int(input("Please enter radius: "))
        print(circle(ask4))

    elif ask == 'rectangular prism':
        ask2 = int(input("Please enter base: "))
        ask3 = int(input("Please enter height: "))
        ask5 = int(input("Please enter lenth: "))
        print(rectangular_prism(rectangle, ask2, ask3, ask5))

    elif ask == 'triangular prism':
        ask2 = int(input("Please enter base: "))
        ask3 = int(input("Please enter height: "))
        ask5 = int(input("Please enter lenth: "))
        print(triangular_prism(triangle, ask2, ask3, ask5))

    elif ask == 'circular prism':
        ask3 = int(input("Please enter height: "))
        ask4 = int(input("Please enter radius: "))
        print(circular_prism(circle, ask3, ask4))

def rectangle(ask2, ask3):
    area = ask2 * ask3
    return(area)

def triangle(ask2, ask3):
    area = ask2 * ask3 / 2
    return(area)

def circle(ask4):
    from math import pi
    area = ask4 * ask4 * pi
    return(area)

def rectangular_prism(rectangle, ask2, ask3, ask5):
    area = rectangle(ask2, ask3) * ask5
    return(area)

def triangular_prism(triangle, ask2, ask3, ask5):
    area = triangle(ask2, ask3) * ask5 / 2
    return(area)

def circular_prism(circle, ask3, ask4):
    from math import pi
    area = circle(ask4) * ask3
    return(area)

#inputs()

#Binary Search
import random

def over_under():
    answer = random.randrange(1, 100)
    win = 0
    while(win == 0):
        print(answer)
        guess = int(input("Over or Under?, 1 - 100: "))
        if guess < answer:
            print("Over")
        elif guess > answer:
            print("Under")
        elif guess == answer:
            win = 1
            print("You got the answer!")

#over_under()

#Binary Search Recursive
import random
answer = random.randrange(1, 100)
def over_under_2():
    print(answer)
    guess = int(input("Over or Under?, 1 - 100: "))
    if guess < answer:
        print("Over")
        over_under_2()
    elif guess > answer:
        print("Under")
        over_under_2()
    elif guess == answer:
        print("You got the answer!")

#over_under_2()

#Binary Search Game / The prototype
import random
max1 = 100
score = 0
answer = random.randrange(1, max1)
def over_under_3():
    global keep_game_run
    global answer
    global score
    global max1
    keep_game_run = 1
    while(keep_game_run == 1):
        print(answer)
        guess = int(input("Over or Under?, 1 - 100+: "))
        if guess == 0:
            print("Thanks For Playing! Final Score =", score)
            keep_game_run = 2
        elif guess < answer:
            print("Over")
        elif guess > answer:
            print("Under")
        elif guess == answer:
            score = score + 1
            max1 = max1 + 100
            print("You got the answer! Keep playing as the range increases by 100! Press 0 to stop!")
            print("Score =", score)
            answer = random.randrange(1, max1)
            over_under_3()
        elif 5 == 6:
            from math import pi
            print(pi)

#over_under_3()

#Binary Search Game Better / The pre-alpha version
#Other Tab

def com():
    #list comprehension
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    list_1 = [var for var in fruits if var != "apple"]
    print(list_1)
    list_2 = [a for a in fruits]
    print(list_2)
    list_3 = [b for b in fruits if len(b) > 5]
    print(list_3)
