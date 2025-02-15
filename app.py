from flask import Flask, request, jsonify
import openai
import sqlite3

app = Flask(__name__)

# OpenAI API Key (Replace with your own key)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize Database
def create_database():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS conversations (user_input TEXT, bot_response TEXT)''')
    conn.commit()
    conn.close()

create_database()

# Function to get AI response
def get_ai_response(user_input):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    
    # Search for similar questions
    cursor.execute("SELECT bot_response FROM conversations WHERE user_input LIKE ?", ('%' + user_input + '%',))
    past_responses = cursor.fetchall()
    conn.close()

    if past_responses:
        return past_responses[0][0]  # Return a past response if found

    # Generate new AI response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    bot_reply = response["choices"][0]["message"]["content"]

    # Save to database
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO conversations (user_input, bot_response) VALUES (?, ?)", (user_input, bot_reply))
    conn.commit()
    conn.close()

    return bot_reply

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data["message"]
    bot_response = get_ai_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
