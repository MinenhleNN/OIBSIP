import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the voice engine 
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%A, %B, %d, %Y")

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenng...")
        audio = r.listen(source)
        try:
            command =r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry I didn't catch that.")
            return""
        except sr.RequestError:
            speak("Sorry, there was a problem with the service.")
            return""

def main():
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        command = listen_command()
        if "hello" in command:
            speak("Hi there!")
        elif "time" in command:
            speak(f"The time is {get_time()}")
        elif "date" in command:
            speak(f"Today's date is {get_date()}")
        elif "search" in command:
            speak(f"What should I search for?")
            query = listen_command()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Here are the search resualts for {query}")
        elif "stop" in command or "exit" in command:
            speak(f"Goodbye!")
            break
                  
main()