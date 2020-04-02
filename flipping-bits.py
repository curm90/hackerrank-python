# https://www.hackerrank.com/challenges/flipping-bits/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous


def flippingBits(n):
    return ~n + (1 << 32)


print(flippingBits(4), 4294967291)
