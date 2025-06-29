
#find 5 different 5 letter word with all different letters

#input / check for possible words (words with all different letters)
possible_words=[]
with open("randwords.txt",'r') as words_txt:
    words=words_txt.readlines()
    for word in words:
        word=word.strip()
        if len(word)==5 and len(set(word))==5:
            possible_words.append(word)

print(possible_words)

#Solution
#Get a word, compare it with next word by adding to larger string.
#if string is unique, continue adding and checking words.
#if there are repeat letters, discard new word and go to next.
#repeat until length string is 25, then change it back to 5 words.

five_words_list=[]
larg_str=""
len_is_25=False
leng_pos_words=len(possible_words)
for word in range(leng_pos_words):
    if len_is_25:
        for i in range(0, 25, 5):
            true_word = larg_str[i:i+5]
            five_words_list.append(true_word)
        break
    larg_str="" #reset if word doesn't have ANY matches
    larg_str+=possible_words[word]
    for nextword in range(word+1,leng_pos_words):
        larg_str+=possible_words[nextword]
        if len(set(larg_str))==len(larg_str):
            if len(larg_str)==25:
                len_is_25=True
                break
            continue
        larg_str=larg_str[:-5]

print(five_words_list)