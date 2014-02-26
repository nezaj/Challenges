#!/usr/bin/env python

# Author: nezaj
# Date: 02/20/14
# Source-File

# http://www.reddit.com/r/dailyprogrammer/comments/1v4cjd/011314_challenge_148_easy_combination_lock/
# [01/13/14] Challenge #148 [Easy] Combination Lock

def clean_params(params):
    """
    Converts a space delimited string of numbers and converts them
    into an array of integers
    """
    if isinstance(params, str):
        params = map(int, params.split(' '))

    return params

def clockwise_turns(n, start, stop):
    """
    Returns number of clockwise turns from start to stop.

    If the stop is after the start the number of turns
    is just the difference between the two.

    If the stop is before the start than we need to turn
    all the way to the end first and turn to the stopping point.
    """
    return (stop - start) if (stop >= start) else (n - start) + stop

def counter_clockwise_turns(n, start, stop):
    """
    Returns number of counter-clockwise turns from start to stop.

    The number of counter-clockwise turns can be thought of in terms
    of clockwise turns. It is equivalent to the difference between
    the number of turns in a full rotation and the number of clockwise turns
    from start to stop
    """
    return 0 if start == stop else n - clockwise_turns(n, start, stop)

def get_combo_turns(n, first, second, third, start=0):
    " Returns total number of turns for locker combination "
    turns = 2 * n
    turns += clockwise_turns(n, start, first)
    turns += n
    turns += counter_clockwise_turns(n, first, second)
    turns += clockwise_turns(n, second, third)

    return turns

def main():
    params = clean_params(raw_input("Enter input: "))
    print get_combo_turns(*params)

if __name__ == "__main__":
    main()
