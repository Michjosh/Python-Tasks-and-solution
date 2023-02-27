import re


def is_safe(x):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{6,}$'
    return bool(re.match(regex, x))


password = input("enter your password: ")
if is_safe(password):
    print("Password is safe!")
else:
    print("Password is not safe.")


