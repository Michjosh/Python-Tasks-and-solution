def is_palindrome(s):
    # Convert the string to lowercase and remove all non-alphanumeric characters
    alphanumeric_string = ''.join(ch.lower() for ch in s if ch.isalnum())

    # Check if the alphanumeric string is equal to its reverse
    return alphanumeric_string == alphanumeric_string[::-1]


phrase = "A man, a plan, a canal: Panama"
print(is_palindrome(phrase))


"""
def is_palindrome(s):
    # Convert the string to lowercase and remove all non-alphanumeric characters
    alphanumeric_string = ''
    for ch in s:
        if ch.isalnum():
            alphanumeric_string += ch.lower()

    # Check if the alphanumeric string is equal to its reverse
    reverse_string = ''
    for i in range(len(alphanumeric_string) - 1, -1, -1):
        reverse_string += alphanumeric_string[i]
    return alphanumeric_string == reverse_string

"""

