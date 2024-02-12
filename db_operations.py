import sqlite3

class DB: 
    def getQuestions(self):
        print("[INVOKED] DB::getQuestions");
        conn = sqlite3.connect("database.db");
        cur = conn.cursor();
        cur.execute("SELECT * FROM questions");
        questions = cur.fetchall();
        questionList = []
        for question in questions:
            print(question);
            questionList.append({
                "qid":question[0],
                "question": question[1],
                "category": question[2],
                "sub-category": question[3],
            });
        return questionList

    def getAnswers(self, quetionId):
        print("[INVOKED] DB::getAnswers");
        conn = sqlite3.connect("database.db");
        cur = conn.cursor();
        cur.execute("SELECT * FROM answers WHERE question_id=?", (quetionId,));
        answers = cur.fetchall();
        answersList = []
        for answer in answers:
            print(answer[1]);
            answersList.append({
                "aid":answer[0],
                "answer":answer[2],
                "question_id":answer[1],
            });
        return answersList