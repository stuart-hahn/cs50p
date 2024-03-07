def get_guess():
    guess = int(input("Guess a number between 1 and 10: ").strip())
    return guess


def main():
    guess = get_guess()
    if guess == 2:
        print("Correct!")
    else:
        print("Incorrect.")


main()
