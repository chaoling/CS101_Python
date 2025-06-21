while True:
    words = input("Saying something: ").lower()
    #print(words)
    if "hello" in words:
        print("Hello to you too!")
    elif "hi" in words:
        print("hi")
    elif "how are you" in words:
        print("I am well, thanks")
    elif any(["goodby" in words, "bye" in words, "再见" in words, "(｡◕‿◕｡)" in words]):
        print("Goodbye to you too!")
        break
    else:
        print("Huh?")
