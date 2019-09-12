from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    # TODO - you fill in here.
    if x == 0:
        return '0'
    ret_val = ''
    while x != 0:
        x, remainder = divmod(x, 10)
        ret_val = chr(remainder+48) + ret_val
    return ret_val


def string_to_int(s):
    # TODO - you fill in here.
    ret_val = 0
    j = len(s)-1
    for i in range(len(s)):
        ret_val += (ord(s[i])-48) * (10 ** j)
        j -= 1
    return ret_val


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
