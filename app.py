import json
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from db_operations import DB

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@app.route('/api/questions/')
@cross_origin()
def get_questions():
    print("[INVOKED] route::get_questions")
    data = DB().getQuestions()
    return jsonify(data)


@app.route('/api/answer/<int:questionId>')
@cross_origin()
def get_answers_for_question(questionId):
    print("[INVOKED] route::get_get_answers_for_question")
    data = DB().getAnswers(questionId)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)