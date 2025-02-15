import requests

# Hugging Face API Key
HUGGING_FACE_API_KEY = "your_huggingface_api_key"

# Define the Hugging Face model endpoint
MODEL_ENDPOINT = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"

# Function to generate AI responses
def get_response(user_message):
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    payload = {"inputs": user_message}

    response = requests.post(MODEL_ENDPOINT, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return "Sorry, I'm having trouble processing your request."
