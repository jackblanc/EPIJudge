from test_framework import generic_test


# Brute Force Approach - O(n) runtime
# def parity(x: int) -> int:
#     num_bits = 0
#     while x:
#         num_bits += x & 1
#         x >>= 1
#     return num_bits % 2 == 1

# A good trick to know is that: x & (x - 1) == x with its lowest set bit erased
# For example, 0010101 & 0010100 == 0010100
# This can improve runtime to O(k), where k == the number of 1 bits
def parity(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= (x - 1)
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
