def main():
    user_input = input("I'm ChAtGpT 🤪 'sup? ").strip().lower()
    greet(user_input)


def greet(input):
    if "hello" in input:
        print("Hello, there!")
    else:
        print("I'm not sure what you mean.")


main()
