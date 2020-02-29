# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings


def makeAnagram(a, b):
    list_a = list(a)
    result_list = []

    for letter in b:
        if letter in list_a:
            list_a.remove(letter)
        else:
            result_list.append(letter)

    return len(list_a) + len(result_list)
