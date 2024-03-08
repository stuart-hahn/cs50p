def main():
    guess = get_guess()
    if guess.strip() == "42":
        print("Yes")
    elif guess.strip().lower() == "forty-two":
        print("Yes")
    elif guess.strip().lower() == "forty two":
        print("Yes")
    else:
        print("No")


def get_guess():
    guess = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    return guess


main()
