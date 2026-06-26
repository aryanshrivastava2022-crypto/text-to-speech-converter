pip install pyttsx3

import pyttsx3

# Install eSpeak-ng, a speech synthesis engine required by pyttsx3
!sudo apt-get update && sudo apt-get install -y espeak-ng

# Initialize the speech engine
engine = pyttsx3.init()

print("🔊 Text-to-Speech Converter")

text = input("Enter the text you want to convert to speech:\n")

# Convert text to speech
engine.say(text)
engine.runAndWait()

print("✅ Speech playback completed!")
