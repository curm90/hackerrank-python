# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

from collections import Counter


def isValid(s):
    # frequencies of all letters
    freq = Counter(s)
    # frequencies values sorted
    values = sorted(freq.values())
    # max frequencie value
    v_max = max(values)
    # min frequencie value
    v_min = min(values)
    # max frequencie value repetitions
    max_count = values.count(v_max)
    # min frequencie value repetitions
    min_count = values.count(v_min)
    # frequencie of frequencie values, made some validations more easy
    freq_values = Counter(values)
    # more then 2 frequencies repeat, this case string can be valid, case: aaabbc
    if len(freq_values) > 2:
        return 'NO'
    # only 1 frequencie repeat, so, is a valid string, case: aabbcc
    elif len(freq_values) == 1:
        return 'YES'
    # min frequencie count is 1, so, just remove one value to turn the string valid, case: aab
    elif min_count == 1:
        return 'YES'
    # max frequencie minus your repeatitions equal min value, case: bbaaa, just remove
    # one of the same letter repeatitions to turn the strig valid
    elif v_max - max_count == v_min:
        return 'YES'
    # other cases are not valids
    else:
        return 'NO'


# TOO SLOW
# def isValid(s):
#     counter = {}
#     arr = []
#     counter_two = {}
#     second_arr = []

#     for char in s:
#         if char in counter:
#             counter[char] += 1
#         else:
#             counter[char] = 1

#     for val in counter.values():
#         arr.append(val)

#     highest_num = max(arr)
#     lowest_num = min(arr)

#     if highest_num - lowest_num > 1:
#         return ('NO')

#     for num in arr:
#         if num in counter_two:
#             counter_two[num] += 1
#         else:
#             counter_two[num] = 1

#     for val in counter_two.values():
#         second_arr.append(val)

#     if min(second_arr) > 1:
#         return ('NO')
#     return ('YES')


print(isValid('aabbcd'), 'NO')
print(isValid('aabbccddeefghi'), 'NO')
print(isValid('abcdefghhgfedecba'), 'YES')
print(isValid('a'), 'YES')
print(isValid('aaaabbcc'), 'NO')
