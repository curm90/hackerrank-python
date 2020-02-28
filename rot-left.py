# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


def rotLeft(arr, rotations):
    # if a is equal to length of d
    if rotations == len(arr):
        # return d
        return arr

    # num_of_rotations = a
    # while a > 0
    while rotations > 0:
        # pop off first value
        first = arr.pop(0)
        # append it to the end
        arr.append(first)
        # decrement a
        rotations -= 1

    # return d
    return arr

# def rotLeft(a, d):
#     return a[d:] + a[:d]


rotLeft(4, [1, 2, 3, 4, 5])
