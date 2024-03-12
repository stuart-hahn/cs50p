# """
# Implement a program that prompts the user for items, one per line,
# until the user inputs control-d (which is a common way of ending one's input to a program).
# Then output the user's grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item. No need to
# pluralize the items. Treat the user's input case-insensitively.
# """


# def get_items():
#     """
#     Get the next grocery item from the user.

#     Args: None

#     Returns:
#         dictionary of items (dict): A dictionary representing the item and the count.
#     """
#     items = {"BANANA": 1}
#     try:
#         while True:
#             item = input("What do you want to add to the list? ").strip().upper()
#             if item not in items:
#                 items[item] = 1
#             else:
#                 items[item] += 1
#     except EOFError:
#         pass

#     print("\nYour Grocery List: ")
#     for item in items:
#         print(f"{item}: {items[item]}")


# get_items()


def main():
    grocery_list = {}

    # Prompt the user for items
    print(
        "Enter your grocery list (one item per line). Press Ctrl+D (Ctrl+Z on Windows) to end input."
    )
    try:
        while True:
            item = input().strip().lower()  # Case-insensitive handling
            if item:
                grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass  # Ctrl+D pressed, end input

    # Output the grocery list
    print("\nYour Grocery List:")
    for item, count in sorted(grocery_list.items(), key=lambda x: x[0]):
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()
