# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


def countingValleys(n, arr):
    sea_level = 0
    result = 0

    for i in range(n):
        if arr[i] == 'U':
            sea_level += 1
            if sea_level == 0:
                result += 1
        else:
            sea_level -= 1

    return result


print(countingValleys(8, ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']), 1)
