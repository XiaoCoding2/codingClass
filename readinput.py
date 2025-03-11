import random

def read_random_word():
    with open("words.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array)
    
word = read_random_word()
print(word)

