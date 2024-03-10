def main():
    user_input = input("Variable name in camelCase: ").strip()
    convert_from_camel_to_snake(user_input)


def convert_from_camel_to_snake(variable_name):
    snake_case = ""
    for character in variable_name:
        if character.lower() == character:
            snake_case += character
        else:
            snake_case += f"_{character.lower()}"
    print(snake_case)


if __name__ == "__main__":
    main()
