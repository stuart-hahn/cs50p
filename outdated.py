def is_valid_date(date):
    """
    Check if the given date is valid in month-day-year or month day, year format.
    """
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    parts = date.split("/")
    if len(parts) != 3:
        return False

    month, day, year = parts
    if not month.isdigit():
        if month.capitalize() not in months:
            return False
        month = str(months.index(month.capitalize()) + 1)

    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    month, day, year = int(month), int(day), int(year)
    if month < 1 or month > 12 or day < 1 or day > 31:
        return False

    return True


def convert_to_iso(date):
    """
    Convert the given date to YYYY-MM-DD format.
    """
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    parts = date.split("/")
    month, day, year = parts
    if not month.isdigit():
        month = str(months.index(month.capitalize()) + 1)
    month = month.zfill(2)
    day = day.zfill(2)
    year = year.zfill(4)

    return f"{year}-{month}-{day}"


def main():
    while True:
        user_input = input("Enter a date (month/day/year or month day, year): ")
        if is_valid_date(user_input):
            iso_date = convert_to_iso(user_input)
            print(f"Date in YYYY-MM-DD format: {iso_date}")
            break
        else:
            print("Invalid date format. Please enter again.")


if __name__ == "__main__":
    main()
