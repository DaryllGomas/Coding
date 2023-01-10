import speech_recognition as sr
import pyttsx3

# Set up speech recognition
r = sr.Recognizer()

# Set up text-to-speech
engine = pyttsx3.init()

# Listen for the user's voice input
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

# Convert the audio to text
text = r.recognize_google(audio)
print("You said: " + text)

# Generate a response
response = "Hello, how are you today?"

# Convert the response to speech
engine.say(response)
engine.runAndWait()

import tkinter as tk

# Create the window
window = tk.Tk()
window.title("Voice Interface")

# Create a canvas to draw the red light on
canvas = tk.Canvas(window, width=200, height=100)
canvas.pack()

# Draw a red circle on the canvas to represent the light
light = canvas.create_oval(50, 50, 150, 150, fill="red")

# Run the Tkinter event loop
window.mainloop()
