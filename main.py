import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak a message
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand what you said.")
    except sr.RequestError as e:
        speak(f"Sorry, there was an error with the speech recognition service: {e}")

# Define a function to handle different voice commands
def handle_command(command):
    if "set a reminder" in command:
        # Code to set a reminder
        speak("Reminder set!")
    elif "create a to-do list" in command:
        # Code to create a to-do list
        speak("To-do list created!")
    elif "search the web" in command:
        # Code to search the web
        speak("Searching the web!")

# Main loop to listen for voice commands
while True:
    command = recognize_speech()
    if command:
        handle_command(command)
