# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=next-challenge&h_v=zen


def birthdayCakeCandles(arr):
    # Place to store the count
    count = 1
    # Sort array highest to lowest
    arr.sort(reverse=True)
    print(arr)
    # Place to store highest num arr[0]
    highest_num = arr[0]
    # iterate over array from first index
    for i in range(1, len(arr)):
        # if arr[i] == to highest num
        if arr[i] == highest_num:
            # Increment count
            count += 1
    # Return count
    return count


print(birthdayCakeCandles([3, 2, 1, 3]), 2)
print(birthdayCakeCandles([4, 4, 1, 3]), 2)
