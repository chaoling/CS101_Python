import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something: ")
    audio = recognizer.listen(source)

print("You said: ")
words = recognizer.recognize_google(audio)
print(words)

#######
# now speak instead of print on the screen
engine = pyttsx3.init()
engine.say("you said: {}".format(words))
engine.runAndWait()

#words = input("Saying something: ").lower()

if "hello" in words:
    engine.say("Hello to you too!")
    engine.runAndWait()
elif "how are you" in words:
    engine.say("I am well, thanks")
    engine.runAndWait()
elif "goodby" in words:
    engine.say("Goodbye to you too!")
    engine.runAndWait()
else:
    engine.say("Huh?")
    engine.runAndWait()

