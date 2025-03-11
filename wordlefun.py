from termcolor import colored
#import random
#print(colored('This text is green', 'green'))
#print(colored('This text is yellow', 'yellow'))
#print(colored('This text is red', 'red'))
chances = 0
def find(word_str, word_com,):
    global chances
    if word_com == word_str:
        print(colored(word_com, 'green'))
        print(f"You Win! You got it in {chances + 1} guesses!")
        chances = 7
    else:
        chances = chances + 1
        for w in range(0, len(word_str)):
            if word_str[w] == word_com[w]:
                print(colored(word_com[w], 'green'), end = '')
            elif word_com[w] in word_str:
                print(colored(word_com[w], 'yellow'), end = '')
            else:
                print(word_com[w], end = '')

#while(chances < 7):
#    print("\nWhat is your guess?:")
#    find("bugle", input())
file_name = input("file name: ")
f = open(file_name)
words = f.read().splitlines()
print(words)

#game I played 6/23/2024
#items
#items e = yellow
#What is your guess?:
#ether
#ether both e = yellow #Normal wordle second e = gray
#What is your guess?:
#backs
#backs b = green
#What is your guess?:
#bodle
#bodle b, l, e = green
#What is your guess?:
#bugle
#bugle all = correct