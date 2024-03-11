def main():
    # create list of dictionaries of fruit:calories
    fruits = {"apple": 130, "avocado": 50, "banana": 110}

    # find the fruit a user requests and display the calories
    request = input("What fruit? ").strip()
    for fruit in fruits:
        if request == fruit:
            print(fruits.get(fruit))


if __name__ == "__main__":
    main()
