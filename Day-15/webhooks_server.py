from flask import Flask, request

app = Flask(__name__)

# Root path to check if the server is running
@app.route("/", methods=["GET"])
def health_check():
    return " Server is running!"

# Webhook path to receive GitHub comment events
@app.route("/webhook", methods=["POST"])
def handle_webhook():
    data = request.json  # Get the JSON payload
    print("Received webhook:")
    print(data)  # Print the GitHub comment data to console
    return "Webhook received!", 200

if __name__ == "__main__":
    app.run(port=5000)
# To run the server, use the command: python webhooks_server.py
# Ensure Flask is installed in your environment: pip install Flask