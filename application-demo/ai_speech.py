import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something: ")
    audio = recognizer.listen(source)

print("You said: ")
words = recognizer.recognize_google(audio)
print(words)

#words = input("Saying something: ").lower()

if "hello" in words:
    print("Hello to you too!")
elif "how are you" in words:
    print("I am well, thanks")
elif "goodby" in words:
    print("Goodbye to you too!")
else:
    print("Huh?")

