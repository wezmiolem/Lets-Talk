from flask import Flask, render_template
import util

app = Flask(__name__)


@app.route('/')
def index():
    questions = util.get_questions()
    question_types = util.get_question_types(questions)
    answers = util.get_answers()
    return render_template('index.html', question_types=question_types, questions=questions, answers=answers)


@app.route('/list/<category>')
def list_of_questions(category):
    questions = util.get_questions()
    question_headers = util.get_question_headers()
    questions_of_category = util.get_questions_of_category(questions, category)
    return render_template('list_of_questions.html', questions_of_category=questions_of_category,
                           question_headers=question_headers, category=category)


@app.route('questions/<question_id>')
def question_and_answers(question_id):
    pass


if __name__ == '__main__':
    app.run()
