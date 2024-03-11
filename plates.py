def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if string length is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Check if first two characters are alphabetic
    if not s[:2].isalpha():
        return False

    # check if all characters are alphanumeric
    if not s.isalnum():
        return False

    # check that plate does not end with 0
    if s[-1] == "0":
        return False

    # check that all characters after 1st digit are also digits
    # for every character in the string...
    for char in s:
        # if the character is a digit...
        if char.isdigit():
            # check if every character after it is also a digit
            # s[s.index(char):].isdigit()
            return True if s[s.index(char) :].isdigit() else False

    return True


main()
