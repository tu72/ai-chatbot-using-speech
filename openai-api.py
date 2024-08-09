import os
os.environ["OPENAI_API_KEY"] = "your_actual_api_key_here"  # Replace with your actual API key DO NOT SHARE WITH OTHERS!!!
from openai import OpenAI
import pyttsx3
import whisper
import pyaudio
import numpy as np
import torch 

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Load Whisper model
model = whisper.load_model("base").to("cpu")

def get_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

def speak_text(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen_for_speech():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 5

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Listening...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Processing...")
    stream.stop_stream()
    stream.close()
    p.terminate()

    audio = np.frombuffer(b''.join(frames), np.int16).astype(np.float32) / 32768.0
    result = model.transcribe(audio, fp16=False)  # Explicitly use FP32, this will make it slower but avoids annoying warnings.
    text = result["text"].strip()
    print(f"You said: {text}")
    return text

def main():
    print("Welcome to the AI chatbot. Say 'quit' to exit.")
    speak_text("Welcome to the AI chatbot. Say 'quit' to exit.")
   
    while True:
        user_input = listen_for_speech()
       
        if user_input.lower() == 'quit':
            print("Goodbye!")
            speak_text("Goodbye!")
            break
       
        ai_response = get_ai_response(user_input)
        print("AI:", ai_response)
        speak_text(ai_response)

if __name__ == "__main__":
    main()