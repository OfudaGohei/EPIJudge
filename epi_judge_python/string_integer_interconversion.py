from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    # TODO - you fill in here.
    if x == 0:
        return '0'
    ret_val = ''
    neg = False
    if x < 0:
        neg = True
        x = x * -1
    while x != 0:
        x, remainder = divmod(x, 10)
        ret_val = chr(remainder+48) + ret_val
    if neg == True:
        ret_val = '-' + ret_val
    return ret_val


def string_to_int(s):
    # TODO - you fill in here.
    neg = False
    ret_val = 0
    if s[0] == '-':
        neg = True
        s = s[1:len(s)]
    j = len(s)-1
    for i in range(len(s)):
        ret_val += (ord(s[j])-48) * (10 ** i)
        j -= 1
    if neg:
        ret_val *= -1
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
