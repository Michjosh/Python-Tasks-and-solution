# 1. Create a list named food with two elements "rice" and "beans". 2. Append the string "broccoli" to food using
# .append(). 3. Add the string "bread" and "pizza" to "food" using .extend(). 4. Print the first two items in the
# food list using print() and slicing notation. 5. Print the last item in food using print() and index notation. 6.
# Create a list called breakfast from the string "eggs, fruit, orange juice" using the string .split() method. 7.
# Verify that breakfast has three items using len(). 8. Create a new list called lengths using a list comprehension
# that contains the lengths of each string in the breakfast list.

food = ["rice", "beans", "broccoli"]

food.extend("pizza food")

print(food[0:2])

print(food[3])

breakfast = "eggs, fruit, orange juice"
new = breakfast.split()

print(new)
print(len(new))

