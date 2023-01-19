import speech_recognition as sr
from gtts import gTTS
import openai
import winsound

# Set your API key
openai.api_key = "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"

def listen_for_prompt():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for prompt...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            if text.lower() == "computer":
                listen_for_input()
    except Exception as e:
        print(f'Error occurred: {e}')
        listen_for_prompt()

def listen_for_input():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for input...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            response = chatGPT_response(text)
            speak_response(response.response)
    except Exception as e:
        print(f'Error occurred: {e}')
        listen_for_input()


def chatGPT_response(text):
    # Use the OpenAI API to get a response from ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(text)
    )
    return response

def speak_response(response):
    if 'response' in response:
        response_text = response.response
        tts = gTTS(response_text)
        tts.save("response.mp3")
        winsound.PlaySound("response.mp3", winsound.SND_FILENAME)
    else:
        print("No response from ChatGPT")




# Start the program by listening for the prompt
listen_for_prompt()
