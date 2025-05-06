from termcolor import colored
import random
#print(colored('This text is green', 'green'))
#print(colored('This text is yellow', 'yellow'))
#print(colored('This text is red', 'red'))

def read_random_word():
    with open("words.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array)
    
word = read_random_word()
chances = 0
def wordle(word_str, word_com,):
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
def wordle_activate():
    print("Welcome to python wordle!")
    while(chances < 7):
        print("\nWhat is your guess?:")
        wordle(word, input())

wordle_activate()

#sys.stdout.write('\x1b[1A')
#sys.stdout.write('\x1b[2K')

