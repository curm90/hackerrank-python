# hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting


def maximum_toys(prices, k):
    # Sort prices
    prices.sort()
    # Place to store number of toys
    num_toys = 0
    # Place to store current total
    current_total = prices[0]

    # Iterate over prices
    for i in range(1, len(prices)):
        # if current_total < k
        if current_total < k:
           # increment num_toys
            num_toys += 1
           # Add prices[i] to current_total
            current_total += prices[i]
        # else
          # return num_toys
    return num_toys


print(maximum_toys([1, 12, 5, 111, 200, 1000, 10], 50)), 4
