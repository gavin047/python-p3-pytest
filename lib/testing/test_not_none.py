#!/usr/bin/env python3

from not_none_functions import return_not_none

# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False
def test_return_not_none():
    result = return_not_none()
    assert result is not None, "The function should not return None"
# This test checks that the return_not_none function returns a value that is not None.

def return_not_none():
    return "This is not None"
# this returns a string which ensures it doesnt return "None"
