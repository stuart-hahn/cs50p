# implement a program that prompts the user for a str of text and then
# outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

# Example input: Twitter
# output: Twttr

# def main():
#     user_input = input("Input: ").strip()
#     vowels = ["A", "E", "I", "O", "U"]
#     tweet = ""
#     for letter in range(len(user_input)):
#         if user_input[letter].upper() in vowels:
#             tweet += ""
#         else:
#             tweet += user_input[letter]

#     print(tweet)


# if __name__ == "__main__":
#     main()


def main():
    text = input("Input: ")
    text_without_vowels = remove_vowels(text)
    print(text_without_vowels)


def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return "".join(char for char in text if char not in vowels)


if __name__ == "__main__":
    main()
