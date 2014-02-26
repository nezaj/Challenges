#!/usr/bin/env python

# Author: nezaj
# Date: 02/26/14
# Test-File

# http://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/
# [02/24/14] Challenge #149 [Easy] Disemvoweler

from disemvoweler import remove_whitespaces, disemvowel

def is_eq(act, exp):
    assert act == exp, "Expected {} got {}".format(exp, act)

def test_remove_whitespaces():
    tc_1 = "hello world"
    exp = "helloworld"
    act = remove_whitespaces(tc_1)
    is_eq(act, exp)

    tc_2 = "     c      "
    exp = "c"
    act = remove_whitespaces(tc_2)
    is_eq(act, exp)


    tc_3 = " "
    exp = ""
    act = remove_whitespaces(tc_3)
    is_eq(act, exp)

def test_disemvowel():
    tc_1 = remove_whitespaces("all those who believe in psychokinesis raise my hand")
    exp = "llthswhblvnpsychknssrsmyhnd", "aoeoeieeioieiaiea"
    act = disemvowel(tc_1)
    is_eq(act, exp)

    tc_2 = remove_whitespaces("did you hear about the excellent farmer who was outstanding in his field")
    exp = "ddyhrbtthxcllntfrmrwhwststndngnhsfld", "ioueaaoueeeeaeoaouaiiiie"
    act = disemvowel(tc_2)
    is_eq(act, exp)

def run_tests():
    test_remove_whitespaces()
    test_disemvowel()

def main():
    run_tests()
    print "All tests pass!"

if __name__ == "__main__":
    main()
