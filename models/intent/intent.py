from flask import Flask, request, jsonify
from rasa_nlu.model import Interpreter

# Initialize the Flask application
app = Flask(__name__)
port = 5002

# load the trained model
model_directory = "./user_input_classifier/model1/default/user_input_classifer"
user_input_clf = Interpreter.load(model_directory)

@app.route('/')
def index():
    return "Intent Classifier API is running."

@app.route('/intent', methods=['POST'])
def predict_api():
    """
    receives a json request with a text field and returns a json response with the intent
    """
    sentence = request.json.get('text')
    intent = user_input_clf.parse(sentence)
    name = intent.get('intent')['name']
    return jsonify({'intent': name})

app.run(host='0.0.0.0', port=port, debug=False)