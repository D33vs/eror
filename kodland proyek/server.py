from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend access

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint for chatbot communication.
    Expects a JSON payload with 'message' from the frontend.
    """
    try:
        # Get the user message from the request
        user_message = request.json.get("message")

        # Make a request to OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model to use
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
        )

        # Extract the bot's reply
        bot_reply = response.choices[0].message["content"]

        # Return the reply to the frontend
        return jsonify({"reply": bot_reply})

    except Exception as e:
        # Handle errors
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong, please try again later."}), 500

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
