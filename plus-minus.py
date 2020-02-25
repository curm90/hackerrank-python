# https://www.hackerrank.com/challenges/plus-minus/problem


def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    zero_count = 0
    length = len(arr)

    for item in arr:
        if item == 0:
            zero_count += 1 / length
        elif item > 0:
            pos_count += 1 / length
        else:
            neg_count += 1 / length

    print(pos_count)
    print(neg_count)
    print(zero_count)


print(plusMinus([-4, 3, -9, 0, 4, 1]), '\n',
      0.500000, '\n', 0.333333, '\n', 0.166667)
