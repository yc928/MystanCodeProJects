"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global
dict_list = []


def main():
    """
    This program will find all anagrams.
    User can input words to check it.
    """
    print("Welcome to stanCode \"Anagram Generator\" (or " + str(EXIT) + ' to quit)')
    data = input('Find anagrams for: ')
    while data != EXIT:
        start = time.time()
        find_anagrams(data)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
        data = input('Find anagrams for: ')


def read_dictionary(s):
    # Sorted the words
    sorted_s = sorted(s)
    # Read the dictionary.txt and leave the similar words
    with open(FILE, 'r') as f:
        global dict_list
        # Same with the for loop below
        dict_list = [line.strip() for line in f if sorted(line.strip()) == sorted_s]
        # print(dict_list)

        # for line in f:
        #     dict_word = line.strip()
        #     if sorted(dict_word) == sorted_s:
        #         dict_list.append(dict_word)


def find_anagrams(s):
    """
    :param s: str, user input
    """
    read_dictionary(s)
    # print(len(dict_list))
    s_list = list(s)
    # print('s_list: ', s_list, s)
    print('Searching...')
    ans = []
    find_anagrams_helper(s_list, [], ans, len(s))
    print(f'{len(ans)} anagrams: {ans}')


def find_anagrams_helper(s_list, current_ans, ans, ans_len):
    """
    :param s_list: list, separate string into list.
    :param current_ans: list, store current char.
    :param ans: list, final answer.
    :param ans_len: int, the length of user input from find_anagrams().
    """
    if has_prefix(current_ans):
        if len(current_ans) == ans_len:
            # Change list to string
            current_word = ''.join(current_ans)
            if current_word in dict_list:
                if current_word not in ans:
                    ans.append(current_word)
                    print('Found: ' + current_word)
                    print('Searching...')
        else:
            for char in s_list:
                # print(current_ans, char, current_ans.count(char), s_list.count(char))
                # Avoid the same char in words
                if current_ans.count(char) == s_list.count(char):
                    pass
                else:
                    # Choose
                    current_ans.append(char)
                    # Explore
                    find_anagrams_helper(s_list, current_ans, ans, ans_len)
                    # Un-choose
                    current_ans.pop()


def has_prefix(sub_s):
    """
    :param sub_s: list, with current char.
    :return: True
    """
    # Change list to string
    text = ''.join(sub_s)
    for words in dict_list:
        if words.startswith(text):
            return True


if __name__ == '__main__':
    main()
