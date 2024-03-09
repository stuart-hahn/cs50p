def main():
    user_input = int(input("How many times should the cat say meow? ").strip())
    talk(user_input)


def talk(number_of_times):
    count = 0
    while count < number_of_times:
        print("meow")
        count += 1


main()
