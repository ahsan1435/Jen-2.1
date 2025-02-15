from flask import Flask, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json.get("message")
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
