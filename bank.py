def get_greeting():
    user_input = input("Greeting: ")
    return user_input.strip().lower()


def calculate_balance():
    user_input = get_greeting()
    hello_length = len("hello")

    if user_input[:hello_length] == "hello":
        print("$0")
    elif user_input.startswith("h"):
        print("$20")
    else:
        print("$100")


# Solve using .startswith() method
# def calculate_balance():
#     greeting = get_greeting()
#     if greeting.startswith("hello"):
#         print("$0")
#     elif greeting[0] == "h":
#         print("$20")
#     else:
#         print("$100")


# Solve using string slicing
# def calculate_balance():
#     greeting = get_greeting()
#     if greeting[: len("hello")] == "hello":
#         print("$0")
#     elif greeting[0] == "h":
#         print("$20")
#     else:
#         print("$100")


def main():
    calculate_balance()


if __name__ == "__main__":
    main()
