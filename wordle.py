from colorama import Fore
from random import seed
from random import randint
from sys import argv

def main():
    # the words from https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt
    #max number of words in file words is 5757 (5756 when start from 0) all words are 5 letters
    if len(argv) < 2:
        print("Make sure to put a word file for the words.")
        exit(1)
    words = []
    with open(argv[1],'r') as file:
        for letter in file:
                words.append(letter.upper().strip('\n'))
    word = []
   # seed random number generator
# generate some integers and random number
    value = randint(0, 5756)
    wordd = words[value]
# ask user for word:
    for i in range(6):
        while 1:
            word.append(input("5 letter word: ").strip().upper())
            if len(word[i]) == 5:
                break
            word.pop()
        check(word, i, wordd)
    print(f"The word is '{wordd.lower()}'.")

def check(word, counter, wordd):
    #grid
    times = 0
    for i in range(13):  #print the hordorian lines
        if i % 2 == 0:
            print("-" * 11)
        else:
            count = 0
            for j in range(11):  #print the vertical and the letters
                if j % 2 == 0:
                    print("|",end="")
                else:
                    if times <= counter:
                        if word[times][count] == wordd[count]:
                            print(Fore.GREEN + f"{wordd[count]}" + Fore.WHITE,end='')
                        elif word[times][count] in wordd:
                            print(Fore.YELLOW + f"{word[times][count]}" + Fore.WHITE,end='')
                        else:
                            print(word[times][count],end='')
                        count += 1  #count the letters
                    else:
                        print(' ',end='')
            times += 1   #count the words
            print('')
    if wordd == word[counter]:
        print("You Win!")
        exit(1)
main()
