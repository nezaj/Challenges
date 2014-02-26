#!/usr/bin/env python

# Author: nezaj
# Date: 02/26/14
# Source-File

# http://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/
# [02/24/14] Challenge #149 [Easy] Disemvoweler


VOWELS = set(["a", "e", "i", "o", "u"])

def remove_whitespaces(s):
    " Removes all spaces, tabs, newlines, and etc from a string "
    return ''.join(s.split())

def disemvowel(s):
    " Returns a tuple of consonants and vowels of a given string"
    cons = ''.join([c for c in s if c not in VOWELS])
    vows = ''.join([c for c in s if c in VOWELS])
    return cons, vows

def print_output(o):
    " Prints consonants and vowels on a seperate line "
    for s in o:
        print s

def main():
    s = remove_whitespaces(raw_input("Enter Input: "))
    o = disemvowel(s)
    print_output(o)

if __name__ == "__main__":
    main()

