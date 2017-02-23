#! /bin/python3

"""
Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome ↴ .
Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"""

def check_palindrom(word):
    lookup = dict()
    for letter in word:
        if letter not in lookup:
            lookup.update({letter: 1})
        else:
            occurance = lookup[letter]
            lookup.update({letter: occurance+1})
    evens = 0
    odds = 0
    for key in lookup:
        if lookup[key] % 2 == 0:
            evens += 1
        else:
            odds += 1
    if (len(word) % 2 == 0 and odds == 0) or (len(word)%2 == 1 and odds == 1):
        return True
    else:
        return False

def main():
    word = "ababccit"
    if check_palindrom(word):
        print("Palindrom possible")
    else:
        print("Palindrom not possible")

if __name__ == '__main__':
    main()