"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""


def square_sort(arr):
    for i in range(len(arr)):
        arr[i] *= arr[i]

    return sorted(arr)


nums = [-4, -1, 0, 3, 10]
print(square_sort(nums))
