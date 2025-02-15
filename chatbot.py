import os
from transformers import pipeline

# Load API Key from GitHub Secrets
HF_API_KEY = os.getenv("HF_API_KEY")

# Load AI Model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def chat(user_input):
    response = chatbot(user_input, max_length=100, do_sample=True)
    return response[0]['generated_text']

# Test Chatbot
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat(user_input)
        print("Bot:", response)
