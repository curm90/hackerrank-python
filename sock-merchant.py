# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


def sockMerchant(n, arr):
    count = 0
    arr.sort()

    i = 0
    while i < n - 1:
        if arr[i] == arr[i + 1]:
            count += 1
            i += 2
        else:
            i += 1

    return count


print(sockMerchant(9, [10, 10, 10, 10, 20, 20, 20, 30, 50]), 3)
print(sockMerchant(9, [10, 10, 10, 10, 20, 20, 20, 30, 20, 50]), 4)
