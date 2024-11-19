import sounddevice as sd
import numpy as np
import speech_recognition as sr
import time

recognizer = sr.Recognizer()

# Function to capture audio using sounddevice
def record_audio(duration=5, sample_rate=44100):
    # Record the audio
    print("Recording audio...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    return audio

# Function to calculate ambient noise level from recorded audio
def calculate_ambient_noise(audio, sample_rate=44100):
    # Convert audio to numpy array and calculate the root mean square (RMS) as an estimate of noise level
    rms = np.sqrt(np.mean(np.square(audio)))
    return rms

def listen():
    while True:
        # Adjust for ambient noise using sounddevice (record for a brief period)
        print("Adjusting for ambient noise...")
        ambient_noise = record_audio(duration=1)
        noise_level = calculate_ambient_noise(ambient_noise)  # Get the noise level

        # Store the noise level for later use in recognition (optional)
        recognizer.energy_threshold = noise_level  # Use calculated noise level as threshold

        print("Listening for 'Hey printer' command...")

        try:
            # Record the "Hey printer" command
            audio = record_audio(duration=5)
            audio_data = sr.AudioData(audio.tobytes(), 44100, 2)  # Convert raw audio to AudioData
            command = recognizer.recognize_google(audio_data).lower()  # Recognize the command
            print("You said:", command)

            if "hey printer" in command or "a printer" in command:
                print("Listening for content to print...")

                # Record the content to print
                audio = record_audio(duration=5)
                audio_data = sr.AudioData(audio.tobytes(), 44100, 2)
                text = recognizer.recognize_google(audio_data)  # Recognize the content
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
