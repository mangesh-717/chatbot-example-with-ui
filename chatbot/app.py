from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST','GET'])
def chat():
    user_message = request.json.get('message')
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

def get_bot_response(message):
    # Define responses based on user messages
    message = message.lower()
    print(message)
    if "hello" in message:
        return "Hi there! How can I help you with our products today?"
    elif "price" in message:
        return "Let me know the product you're interested in, and I'll check the price for you!"
    elif "shipping" in message:
        return "We offer free shipping for orders above a certain amount. Let me know if you want details!"
    else:
        return "I'm here to assist you with any questions about our clothing collection!"

if __name__ == '__main__':
    app.run(debug=True)
