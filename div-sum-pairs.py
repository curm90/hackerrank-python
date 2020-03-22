# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


def divisibleSumPairs(n, k, ar):
    # place to store the count
    count = 0
    # iterate over arr
    for i in range(0, n - 1):
        # iterate for every num
        for j in range(i + 1, n):
            # if i < j and arr[i] + arr[j] % k == 0
            a = ar[i]
            b = ar[j]
            if i < j and (a + b) % k == 0:
                # increment count
                count += 1
    # return count
    return count


print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))
