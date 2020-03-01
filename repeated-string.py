# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


def repeatedString(s, n):
    length = len(s)
    div = n // length
    extra = n % length

    norm = s.count('a')
    total = norm * div

    splice = s[:extra]
    total += splice.count('a')

    return total


print(repeatedString('aba', 10), 7)
