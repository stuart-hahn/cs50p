def main():
    # # 'for' loop to iterate through a list
    # numbers = [1, 2, 3, 4, 5]
    # for num in numbers:
    #     print(num)

    # # 'while' loop to count to 5
    # i = 0
    # while i < 5:
    #     print(i + 1)
    #     i += 1
    # for i in range(5):
    #     print(i)
    # for i in range(10, 0, -1):
    #     print(i)
    # for i in range(0, 10, 2):  # Increment by 2
    #     print(i)
    # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # for i in range(0, len(my_list), 2):  # Access every other element
    #     print(my_list[i])
    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits):
        print(index, fruit)


if __name__ == "__main__":
    main()
