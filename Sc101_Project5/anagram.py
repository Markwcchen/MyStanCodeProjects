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


def main():
    """
    TODO:
    """
    print('Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    while True:
        user_input = input('Find anagrams for:')
        if user_input == EXIT:
            break
        else:
            start = time.time()
            dictionary = read_dictionary()
            anagrams = find_anagrams(user_input, dictionary)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################


def read_dictionary():
    dictionary = []
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            dictionary.append(word)
    return dictionary


def find_anagrams(s, dictionary):
    """
    :param s:
    :return:
    """
    anagrams = []
    print('Searching...')
    find_anagrams_helper(s, '', dictionary, anagrams)
    print('Search completed.')
    print_anagrams(anagrams)
    return anagrams


def find_anagrams_helper(remaining, current, dictionary, anagrams):
    if len(remaining) == 0 and current not in anagrams and current in dictionary:
        anagrams.append(current)
        print(f'Found: {current}')
    else:
        for i in range(len(remaining)):
            next_char = remaining[i]
            rest = remaining[:i] + remaining[i+1:]
            if has_prefix(current+next_char, dictionary):
                find_anagrams_helper(rest, current + next_char, dictionary, anagrams)


def has_prefix(sub_s, dictionary):
    """
    :param sub_s:
    :return:
    """
    return any(word.startswith(sub_s) for word in dictionary)


def print_anagrams(anagrams):
    print(f'{len(anagrams)} anagrams: {anagrams}')


if __name__ == '__main__':
    main()
