from pathlib import Path

try:
    file_name = open(Path.cwd(), "w")
    file_name.write("Hello")
    raise IOError
except IOError as e:
    print(e)
else:
    file_name.close()
print("Successful")
#
# try:
#     number = int(input("Kindly enter your card number: "))
# except IOError:
#     print("Enter the right data type")
#
# if number != 16:
#     raise Exception("Incomplete number")
