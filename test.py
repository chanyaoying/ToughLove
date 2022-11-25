from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
port = 5001

# enable cors
CORS(app)


@app.route('/')
def index():
    return "TEST is running."


app.run(host='0.0.0.0', port=port, debug=False)
