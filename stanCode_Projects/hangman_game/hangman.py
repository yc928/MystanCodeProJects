"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program is to guess the words in 7 turns.
    """
    # initial
    word_tmp = ''
    n_turns = N_TURNS
    # get the ans from random function
    ans = random_word()
    # set up the words with '-', same distance with the answer.
    for i in range(len(ans)):
        word_tmp += '-'
    print('The word was: ' + ans)
    print('The word looks like ' + word_tmp)
    print('You have ' + str(n_turns) + ' wrong guesses left.')
    while True:
        # change all input to upper case. (case-insensitive)
        user_guess = input('Your guess: ').upper()
        # only one alphabet allow to input
        if user_guess.isalpha() and len(user_guess) == 1:
            # save the last step word information
            old_word_tmp = word_tmp
            # user input is in the answer or not
            if user_guess in ans:
                print('You are correct!')
                word_tmp = ''
                # find the correct position in the answer and show the correct alphabet
                for i in range(len(ans)):
                    if ans[i] == user_guess:
                        word_tmp += user_guess
                    else:
                        # fill the alphabet that has already shown last step
                        word_tmp += old_word_tmp[i]
            else:
                n_turns -= 1
                print("There is no " + user_guess + "'s" + " in the word.")
            if word_tmp == ans:
                # finish and break
                print('You win')
                break
            if n_turns == 0:
                # end of the game
                print('You are completely hung T_T')
                break
            print('The word looks like ' + word_tmp)
            print('You have ' + str(n_turns) + ' wrong guesses left.')
        else:
            print('Illegal format.')
    print('The word was: ' + ans)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
