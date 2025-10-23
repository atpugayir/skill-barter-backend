from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_chat_response
from recommender import get_recommendations
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/chatbot", methods=["POST"])
def chatbot_api():
    data = request.json
    message = data.get("message", "")
    response = get_chat_response(message)
    return jsonify({"response": response})

@app.route("/recommend", methods=["POST"])
def recommender_api():
    data = request.json
    user_input = data.get("input", "")
    recommendations = get_recommendations(user_input)
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
