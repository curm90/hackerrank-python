# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

from collections import Counter


def checkMagazine(magazine, note):
    note_count = Counter(note)
    mag_count = Counter(magazine)

    if note_count - mag_count == {}:
        return print('Yes')
    return print('No')


print(checkMagazine('ive got a lovely bunch of coconuts',
                    'ive got some coconuts'), 'No')

print(checkMagazine('two times three is not four', 'two times two is four'), 'No')
print(checkMagazine('give me one grand today night', 'give one grand today'), 'Yes')
