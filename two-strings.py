# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


# def twoStrings(s1, s2):
#     if any(letter in s2 for letter in s1):
#         return 'Yes'
#     return 'No'


def twoStrings(s1, s2):
    return 'YES' if any(letter in s2 for letter in s1) else 'NO'


print(twoStrings('hello', 'world'), 'Yes')
print(twoStrings('hi', 'world'), 'No')
