# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


def jumpingOnClouds(c):
    # place to store the count
    count = 0
    # place to store the index
    i = 0
    # while index less than len of arr
    while i < len(c):
        # if i plus 2 less than the length of c and i + 2 is a 0
        if i + 2 < len(c) and c[i + 2] == 0:
            # increment count
            count += 1
            # increment index by 2
            i += 2
        # else if i plus 1 is less than len of c and i + 1 is a 0
        elif i + 1 < len(c) and c[i + 1] == 0:
            # increment count
            count += 1
            # increment index by 1
            i += 1
        # else
        else:
            # increment index by 1
            i += 1

    # return count
    return count


print(jumpingOnClouds([0, 0, 0, 1, 0, 0]), 3)
