# convert_cel_to_far() which takes one float parameter representing
# degrees Celsius and returns a float representing the same
# temperature in degrees Fahrenheit using the following formula:
# F = C * 9/5 + 32

def convert_cel_to_far(celsius):
    f = celsius * (9/5) + 32
    return f


def  convert_far_to_cel(fahrenheit):
    c = (fahrenheit - 32) * (5/9)
    return c


temp_far = input("Enter temperature degree F ")
celsius = convert_far_to_cel(float(temp_far))
print(f"{temp_far} degrees F = {celsius:.2f} degrees C")

temp_cel = input("Enter temperature in degrees C ")
fahrenheit = convert_cel_to_far(float(temp_cel))
print(f"{temp_cel} degrees C = {fahrenheit:.2f} degrees F")




