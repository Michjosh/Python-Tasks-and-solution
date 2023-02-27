# Create the following list [4, 3, 2, 1] and assign it to the variable numbers
#  Create a copy of the numbers list using the [:] slicing notation.
#  Sort the numbers list in numerical order using the .sort() method.

numbers = [4, 3, 2, 1]

new_numbers = numbers[:]

print(new_numbers)

new_numbers.sort()

print(new_numbers)