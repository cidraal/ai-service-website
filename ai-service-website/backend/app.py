from flask import Flask, request, jsonify

print("Starting Flask app...")

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    bot_reply = f"Echo: {user_message}"  # Replace this with AI logic later
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
