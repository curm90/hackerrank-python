# https://www.hackerrank.com/challenges/the-birthday-bar/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


def birthday(s, d, m):
    # Place to store the count
    count = 0
    # Place to store current sum
    sum = 0

    # Iterate over array
    for i in range(0, len(s)):
        # Add val at current index to sum
        sum += s[i]

        # if i is greater than m - 1
        if i >= m - 1:
            # If sum is equal to d
            if sum == d:
                # increment count
                count += 1
            # Reset sum to be the value at the next index
            sum -= s[i - (m - 1)]
    # Return count
    return count


print(birthday([1, 2, 1, 3, 2], 3, 2), 2)
print(birthday([1, 1, 1, 1, 1, 1], 3, 2), 0)
