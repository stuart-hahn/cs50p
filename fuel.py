"""
fuel.py: A program to calculate fuel percentage in a tank.

This program prompts the user for a fraction in the format X/Y,
where X and Y are integers, representing the amount of fuel in the tank.
It then outputs the fuel percentage rounded to the nearest integer.
If the tank is essentially empty (1% or less remains), it outputs 'E'.
If the tank is essentially full (99% or more remains), it outputs 'F'.
"""


def get_fuel_percentage(fraction):
    """
    Calculate the fuel percentage based on the provided fraction.

    Args:
        fraction (str): A string representing the fuel fraction in the format X/Y.

    Returns:
        tuple: A tuple containing the fuel percentage rounded to the nearest integer
        and an error message if applicable.
    """
    try:
        parts = fraction.split("/")  # split the str "fraction" into two parts
        if len(parts) != 2:
            return None, "Invalid fraction format. Please enter again."

        x_str, y_str = (
            parts  # separate the parts of the fraction into variables (still strings)
        )
        if (
            not x_str.isdigit() or not y_str.isdigit()
        ):  # check if x and y are both digits
            return None, "Invalid fraction format. Please enter again."

        x, y = int(x_str), int(y_str)  # convert x and y into ints
        if x <= 0 or y <= 0 or x > y:  # catch invalid fractions
            return None, "Invalid fraction. Please enter again."

        percentage = (x / y) * 100

        if percentage <= 1:
            return "E", None
        elif percentage >= 99:
            return "F", None
        else:
            return round(percentage), None

    except ZeroDivisionError:
        return None, "Denominator cannot be zero. Please enter again."


def main():
    """
    Main function to interact with the user and calculate fuel percentage.
    """
    while True:
        fraction = input("Enter the fuel fraction (in the format X/Y): ")
        percentage, error = get_fuel_percentage(fraction)

        if error:
            print(error)
        elif percentage == "E":
            print("E")
            break
        elif percentage == "F":
            print("F")
            break
        else:
            print(f"The tank is {percentage}% full.")
            break


if __name__ == "__main__":
    main()
