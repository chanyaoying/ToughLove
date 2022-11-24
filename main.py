from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from util import pronoun_substitution
from util import process_output

app = Flask(__name__)
port = 5000

# enable cors
CORS(app)

@app.route('/')
def index():
    return "ToughLove API is running."

@app.route('/get-response/<text>/<withInsult>', methods=["GET"])
def get_response(text, withInsult):
    """
    receives a json request with a text field and returns a json response with the intent
    """

    # get GET parameters
    # user_input = request.args.get('text')

    print("Request received: ", text, "\n")
    text_json = {'text': text}

    if type(withInsult) == str:
        withInsult = withInsult.lower() == 'true'
    
    print("withInsult: ", withInsult)

    if withInsult:
        # send the text to the intent classifier
        intent = requests.post('http://localhost:5002/intent', json=text_json).json()
        print("Intent: ", intent, "\n")
        intent = intent['intent']
        if intent == "Unrelated":
            # send the text to the social chatbot
            predicted_text = requests.post('http://localhost:5001/predict', json=text_json).json()
            return jsonify({'is_insult': False, 'chatbot_response': predicted_text['chatbot_response']})

        # send the text to the insult bot
        # pronoun substitution
        user_input = text_json['text']
        parsed_user_input = pronoun_substitution(user_input)
        generated_insult = requests.post('http://localhost:5003/get-insult', json={'text': parsed_user_input + ", "}).json()
        return jsonify({'is_insult': True, 'insult_data': generated_insult, 'intent': intent})
    else:
        predicted_text = requests.post('http://localhost:5001/predict', json=text_json).json()
        return jsonify({'is_insult': False, 'chatbot_response': predicted_text['chatbot_response']})

app.run(host='0.0.0.0', port=port, debug=False) 