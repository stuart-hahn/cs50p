def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Convert string like "$50.00" to 50.0

    Args:
    dollars (str): Dollars as a string, with leading dollar sign ($)

    Returns:
    float: dollar value
    """
    value = float(d[1:])
    return value


def percent_to_float(p):
    """
    Convert a percent to a float

    Args:
    percent (str): a string that represent a percentage like ##%

    Returns:
    A float that represents the percentage as a decimal (15% would be 0.15)
    """
    value = float(p[:-1]) / 100
    return value


main()
