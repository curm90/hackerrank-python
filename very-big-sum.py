# https://www.hackerrank.com/challenges/a-very-big-sum/problem


def aVeryBigSum(arr):
    result = 0
    for i in arr:
        result += i

    return result


print(aVeryBigSum([1000000001, 1000000002, 1000000003,
                   1000000004, 1000000005]), 5000000015)
