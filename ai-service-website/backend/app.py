import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = ""

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    # Call OpenAI GPT-4 API
    response = openai.Completion.create(
        model = "gpt-4",  # Use GPT-4 model
        prompt = user_message,
        max_tokens = 1000
        temperature = 0.7
    )

    bot_reply = response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
    bot_reply = "Sorry, I couldn't process your request."

    return jsonify({'reply': bot_reply})
    
if __name__ == '__main__':
    app.run(debug=True)
