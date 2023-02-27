def rotate(array, k):
    # make sure k is within the range of the array length
    k = k % len(array)
    # reverse the entire array
    reverse(array, 0, len(array) - 1)
    # reverse the first k elements
    reverse(array, 0, k - 1)
    # reverse the remaining elements
    reverse(array, k, len(array) - 1)

    return array


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

result = rotate(nums, k)

print(result)
