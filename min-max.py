# https://www.hackerrank.com/challenges/mini-max-sum/problem


def miniMaxSum(arr):
    # a place to store min sum
    max_sum = 0
    # a place to store max sum
    min_sum = 0

    min_num = min(arr)
    max_num = max(arr)

    for num in arr:
        max_sum += num
        min_sum += num

    print(min_sum - max_num, max_sum - min_num)


miniMaxSum([7, 69, 2, 221, 8974])
