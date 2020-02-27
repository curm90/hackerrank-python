# https://www.hackerrank.com/challenges/compare-the-triplets/problem


def compareTriplets(a, b):
    a_count = 0
    b_count = 0

    for an, bn in zip(a, b):
        if an > bn:
            a_count += 1
        else:
            if bn > an:
                b_count += 1

    return a_count, b_count


print(compareTriplets((1, 2, 3), (3, 2, 1)), (1, 1))
