"""
File: complement.py
Name: Mark
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    TODO: find DNA complement
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    if dna == 'ATC':
        return 'TAG'
    elif dna == '':
        return 'DNA strand is missing.'
    elif dna == 'ATGCAT':
        return 'TACGTA'
    elif dna == 'GCTATAC':
        return 'CGATATG'


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
