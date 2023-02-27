# 4696660001713124
class CreditCardValidator:
    pass


def get_validity(card_number: str):
    # 1. Change datatype to list[int]
    card_number = [int(num) for num in card_number]
    # 2. Remove the last digit:
    check_digit = card_number.pop(-1)
    # 3. Reverse the remaining digits:
    card_number.reverse()
    # 4. Double digits at even indices
    card_number = [num * 2 if idx % 2 == 0 else num for idx, num in enumerate(card_number)]
    # 5. Subtract 9 at even indices if digit is over 9
    # (or you can add the digits)
    card_number = [num - 9 if idx % 2 == 0 and num > 9 else num for idx, num in enumerate(card_number)]
    # 6. Add the check_digit back to the list:
    card_number.append(check_digit)
    # 7. Sum all digits:
    check_sum = sum(card_number)
    # 8. If check_sum is divisible by 10, it is valid.
    if check_sum % 10 == 0:
        print("**Credit Card Validity Status: Valid")
    else:
        print("**Credit Card Validity Status: Invalid")


def get_card_type(card_number: str):
    if card_number[0] == "4":
        print("**Credit Card Type: Visa Card")
    if card_number[0] == "5":
        print("**Credit Card Type: MasterCard")
    if card_number[0] == "37":
        print("**Credit Card Type: American Express Cards")
    if card_number[0] == "6":
        print("**Credit Card Type: Discover cards")


def get_card_length(card_number: str):
    print("**Credit Card Digit length: ", end="")
    print(len(card_number))


def get_card_number(card_number: str):
    digit = [int(card_number)]
    print("**Credit Card Number: ", end="")
    for i in digit:
        print(i)


number = str(input("Kindly enter your card number: "))

print()
print("***************************************")
get_card_type(number)
get_card_number(number)
get_card_length(number)
get_validity(number)
print("**************************************")
