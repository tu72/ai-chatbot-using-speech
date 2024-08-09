# AI Chatbot with Speech Recognition and Text-to-Speech

This project implements an AI chatbot that uses speech recognition for input and text-to-speech for output, interfacing with OpenAI's GPT-3.5-turbo model for generating responses.

## Prerequisites

- Windows pc/laptop (you can get this to work on macOS/linux but it's not included in the steps)
- Python 3.7+
- An OpenAI API key
- At least 5 USD in your OpenAI account (so the api will work)
- got the [basic ChatBot](https://github.com/tu72/AI-Chatbot-using-OpenAI-API) working 

## Installation

1. Clone this repository or download the `openai-api.py` file.

2. Install the required Python packages:
  ```pip install openai pyttsx3 whisper pyaudio numpy torch```

## Setup

1. Replace the placeholder API key in the script with your actual OpenAI API key:
```python
os.environ["OPENAI_API_KEY"] = "your_actual_api_key_here"
```
Important: Never share your API key publicly.

## Usage
1. Run the script:
   python openai-api.py
2. The chatbot will greet you and wait for your voice input.
3. Speak clearly into your microphone when prompted (listening...).
4. The AI will process your speech, generate a response, and speak it back to you.
5. To exit the program, say "quit".
   
   ![Screenshot 2024-08-09 205105](https://github.com/user-attachments/assets/21894602-741e-49e2-9779-cc967d546663)
