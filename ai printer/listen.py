import speech_recognition as sr
import time

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen():
    while True:
        #this ius working yay
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for 'Hey printer' command...")

            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                print("You said:", command)

                if "hey printer" in command:
                    print("Listening for content to print...")
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio)
                    print("You said:", text)

                    # Return the recognized text
                    return text

            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Moving on...")
                continue
            except sr.RequestError:
                print("Couldn't request results from Google Speech Recognition service")

            # Small pause between listens
            time.sleep(1)
