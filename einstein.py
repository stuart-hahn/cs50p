def prompt_user_for_mass():
    user_input = input("m: ").strip()
    user_input_as_int = int(user_input)
    return user_input_as_int


def convert_to_joules(mass):
    """
    Take a mass in kilograms and convert it using E = mc2

    Args:
        number (int): Mass in kilograms

    Returns:
        number (int): Joules
    """
    E = mass * pow(300000000, 2)
    return E


def main():
    M = prompt_user_for_mass()
    E = convert_to_joules(M)
    print(f"e: {E}")


if __name__ == "__main__":
    main()
