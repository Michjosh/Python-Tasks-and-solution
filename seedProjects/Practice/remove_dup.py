def remove_duplicates(number):
    if not number:
        return 0

    i = 0
    for j in range(1, len(number)):
        if number[j] != number[i]:
            i += 1
            number[i] = number[j]

    return i + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(nums))
