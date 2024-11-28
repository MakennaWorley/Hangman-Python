'''
Hangman.py

Author: Makenna Worley
'''

import sys
import random

from sympy.abc import lamda


class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print(c,end="")
        print()

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        #print word
        #print(word)

        self.wordguess = ['_'] * len(word)

        # printing the word like _ _ _ _ for the user
        self.printword()

        guesses = 0
        used_letters = []
        
        while guesses < 10:
            ch = input('Enter a guess: ').lower()
            
            ### Your code goes here:###
            if ch.isalpha() and ch.__len__() == 1: #guessed character is letter and not empty
                if ch not in used_letters:
                    positions_of_letter = list(map(lambda i: i if word[i] == ch else None, range(len(word)))) #None if not in the letter not in word
                    positions_of_letter = list(filter(lambda val: val is not None, positions_of_letter)) #filter the list

                    if positions_of_letter.__len__() < 1: #letter does not appear in word
                        print(ch, "does not occur")
                    else: #letter appears the word
                        while positions_of_letter.__len__() > 0:
                            #print(positions_of_letter.pop(0)) #index with letter in word
                            self.wordguess[positions_of_letter.pop(0)] = ch

                    self.printword()
                    used_letters.append(ch)
                    guesses += 1
                    print("You have", 10 - guesses, "guesses left.")

                    if '_' not in self.wordguess:
                        print("Congratulations!\nYou took", guesses, "guesses!")
                        return
                else:
                    print("The letter", ch, "has already been used")
            elif ch.isalpha() and ch.__len__() != 1: #only one character is allowed
                print("Only one character is allowed in each input")
            else: #not a letter was typed
                print("Only allow alphabetic characters")

        print("Sorry dude, the word is", word)

if __name__ == "__main__":

    game = Hangman()

    game.playgame()
