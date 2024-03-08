def convert(text):
    """
    Convert :) to 🙂 and :( to 🙁 in the input text.

    Args:
        text (str): Input text.

    Returns:
        str: Text with smileys converted.
    """
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    """
    Main function to prompt user for input, call convert, and print the result.
    """
    user_input = input("Enter a text: ")
    converted_text = convert(user_input)
    print("Converted text:", converted_text)


# Calling the main function
if __name__ == "__main__":
    main()
