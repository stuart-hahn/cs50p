def playback():
    user_input = input("Say something: ")
    slow_user_input = user_input.replace(" ", "...")
    print(slow_user_input)


playback()
