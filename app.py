import json
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Example API route (replace with your specific logic)
@app.route('/')
@cross_origin()
def get_home():
    return "<h1>This is a Backend service for a Knowledeg Project.</h1>"

# Example API route (replace with your specific logic)
@app.route('/api/questions')
@cross_origin()
def get_questions():
    # Open the JSON file in read mode
    with open('question.json', 'r') as f:
        try:
            # Load the JSON data
            data = json.load(f)
        except FileNotFoundError:
            # Handle file not found error (return suitable error response)
            return jsonify({'error': 'JSON file not found'}), 404
        except json.JSONDecodeError:
            # Handle invalid JSON data error (return suitable error response)
            return jsonify({'error': 'Invalid JSON data'}), 400

    # Return the JSON data as a JSON response
    return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)