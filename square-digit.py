def square_digits(num):
    result = ''
    num_string = str(num)

    for n in num_string:
        result += str(int(n) ** 2)
    return int(result)


print(square_digits(9119))
