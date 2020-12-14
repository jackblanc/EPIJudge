from test_framework import generic_test


def reverse(x: int) -> int:
    x_remaining, result = abs(x), 0
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10  # double slash required for integer division
    return -result if x < 0 else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
