import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Add your key in .env

def get_chat_response(message):
    if not message:
        return "Please provide a message."
    try:
        # Example using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
