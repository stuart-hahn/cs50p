def get_greeting():
    greeting = input("Greeting: ")
    return greeting.strip().lower()


def calculate_balance():
    greeting = get_greeting()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")


def main():
    calculate_balance()


main()
