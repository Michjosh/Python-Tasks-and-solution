#  Create a tuple literal named cardinal_numbers that holds the strings
# "first", "second" and "third", in that order.
#  Using index notation and print(), display the string at index 1 in
# cardinal_numbers.
#  Unpack the values in cardinal_numbers into three new strings
# named position1, position2 and position3 in a single line of code,
# then print each value on a separate line.
#  Create a tuple called my_name that contains the letters of your name
# by using tuple() and a string literal.
#  Check whether or not the character "x" is in my_name using the in
# keyword.
#  Create a new tuple containing all but the first letter in my_name using
# slicing notation.

cardinal_numbers = ("first", "second", "third")
print(cardinal_numbers[1])

position1, position2, position3 = cardinal_numbers

print(position1)
print(position2)
print(position3)

my_name = "M","I","C","H"

print("x" in my_name)

my_new_name = my_name[1:4]

print(my_new_name)

print(range(19))
print(list(range(10)))