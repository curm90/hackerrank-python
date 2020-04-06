# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


def hourglassSum(arr):
  # A place to store the result
    result = list()

  # Iterate over array
    for i in range(len(arr) - 2):
        # Iterate over sub array
        for j in range(len(arr) - 2):
            # Append hourglass indexes to result
            result.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1]
                          [j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])

    # Return biggest sum
    return max(result)


print(hourglassSum([
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]))
