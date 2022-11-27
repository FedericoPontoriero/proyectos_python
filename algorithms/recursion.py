# def sum(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total


# print(sum([1, 2, 7, 9]))


def sum(numbers):
    if not numbers:
        return 0
    remaining_sum = sum(numbers[1:])
    return numbers[0] + remaining_sum


print(sum([1, 2, 7, 9]))
