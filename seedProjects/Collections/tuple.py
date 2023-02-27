# 1. Create a tuple data with two values. The first value should be the
# tuple (1, 2) and the second value should be the tuple (3, 4).
# 2. Write a for loop that loops over data and prints the sum of each
# nested tuple. The output should look like this:
# Row 1 sum: 3
# Row 2 sum: 7

numbers = ((1, 2),(3, 4))

for i in numbers:
    print(f"Row 1 sum: {sum(i)}")


