#!/usr/bin/env python

# Author: nezaj
# Date: 02/20/14
# Test-File

from combo_lock import clockwise_turns, counter_clockwise_turns, get_combo_turns

def is_eq(act, exp):
    assert act == exp, "Expected {} got {}".format(exp, act)

def test_clockwise():
    # Turning clockwise from 0 to 0 should take 0 turns
    act_turns = clockwise_turns(5, 0, 0)
    exp_turns = 0
    is_eq(act_turns, exp_turns)

    # Turning clockwise from 1 to 3 should take 2 turns
    act_turns = clockwise_turns(5, 1, 3)
    exp_turns = 2
    is_eq(act_turns, exp_turns)

    # Turning clockwise from 3 to 1 should take 3 turns
    act_turns = clockwise_turns(5, 3, 1)
    exp_turns = 3
    is_eq(act_turns, exp_turns)

def test_counter_clockwise():
    # Turning counter-clockwise from 0 to 0 should take 0 turns
    act_turns = counter_clockwise_turns(5, 0, 0)
    exp_turns = 0
    is_eq(act_turns, exp_turns)

    # Turning counter-clockwise from 1 to 2 should take 4 turns
    act_turns = counter_clockwise_turns(5, 1, 2)
    exp_turns = 4
    is_eq(act_turns, exp_turns)

    # Turning counter-clockwise from 2 to 1 should take 1 turn
    act_turns = counter_clockwise_turns(5, 2, 1)
    exp_turns = 1
    is_eq(act_turns, exp_turns)

def test_get_combo_turns():
    params = [5, 1, 2, 3]

    # Two full turns, clockwise to 1, full turn, counter-clockwise to 2,
    # clockwise to three should take 21 turns
    exp_turns = 21
    act_turns = get_combo_turns(*params)
    is_eq(act_turns, exp_turns)

def run_tests():
    test_clockwise()
    test_counter_clockwise()
    test_get_combo_turns()

def main():
    run_tests()
    print "All tests pass!"

if __name__ == "__main__":
    main()
