"""
File: caesar.py
Name: Mark
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO: decipher the string
    """
    secret_num = int(input('Secret number: '))
    # input the secret number
    test = str(input("What's the ciphered string? "))
    # test word to decipher
    print('The deciphered string is: ', end='')
    test = upper(test)
    # test word to decipher
    first_half = ALPHABET[secret_num:26]
    # first_half = from ? to Z
    second_half = ALPHABET[0:secret_num]
    # second_half = from A to ?
    after = first_half + second_half
    # after = remix the ALPHABET
    for i in range(len(test)):
        n = test[i]
        if n in ALPHABET:
            n = ALPHABET.index(n)
            print(after[n], end='')


def upper(test):
    ans = ''
    for i in range(len(test)):
        ch = test[i]
        if ch.islower():
            ans += ch.upper()
        else:
            ans += ch
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
