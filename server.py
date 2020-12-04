from flask import Flask, render_template, request, redirect, url_for
import util

app = Flask(__name__)


@app.route('/')
def index():
    questions = util.get_questions()
    question_types = util.get_question_types(questions)
    answers = util.get_answers()
    answers_for_each_type = util.num_of_answers_for_each_type(questions, answers)
    return render_template('index.html', question_types=question_types, questions=questions,
                           answers=answers, answers_for_each_type=answers_for_each_type)


@app.route('/list/<category>')
def list_of_questions(category):
    questions = util.get_questions()
    question_headers = util.get_question_headers()
    questions_of_category = util.get_questions_of_category(questions, category)
    return render_template('list_of_questions.html', questions_of_category=questions_of_category,
                           question_headers=question_headers, category=category)


@app.route('/questions/<question_id>')
def question_and_answers(question_id):
    questions = util.get_questions()
    question = util.get_data_by_id(questions, question_id)
    answers = util.get_answers()
    answers_for_question = util.get_answers_for_question(question_id, answers)
    return render_template('question_and_answers.html', question=question,
                           answers_for_question=answers_for_question, question_id=question_id)


@app.route('/add_question')
def add_question():
    return render_template('new_question.html')


@app.route('/add_question/post', methods=['POST'])
def add_question_post():
    question_keys = util.get_question_keys()
    new_question = dict.fromkeys(question_keys, None)
    questions = util.get_questions()
    question_data = dict(request.form)
    question_data['id'] = util.get_new_id(questions)
    question_data['submission_time'] = util.get_current_datetime_string()
    question_data['view_number'] = 0
    question_data['vote_number'] = 0
    new_question.update(question_data)
    util.add_to_data(questions, new_question)
    return redirect(url_for('question_and_answers', question_id=new_question['id']))


@app.route('/questions/<question_id>/new-answer')
def add_answer(question_id):
    return render_template('new_answer.html', question_id=question_id)


@app.route('/questions/<question_id>/new-answer/post', methods=['POST'])
def add_answer_post(question_id):
    answer_keys = util.get_answer_keys()
    new_answer = dict.fromkeys(answer_keys, None)
    answers = util.get_answers()
    answer_data = dict(request.form)
    answer_data['question_id'] = int(question_id)
    answer_data['id'] = util.get_new_id(answers)
    answer_data['submission_time'] = util.get_current_datetime_string()
    answer_data['vote_number'] = 0
    new_answer.update(answer_data)
    util.add_to_data(answers, new_answer)
    return redirect(url_for('question_and_answers', question_id=question_id))


@app.route('/question/<answer_id>/vote_up')
def add_answer_rating(answer_id):
    answers = util.get_answers()
    listed_answer = util.get_data_by_id(answers, answer_id)
    answer_to_change = listed_answer[0]
    answer_to_change['vote_number'] += 1
    question_id = answer_to_change['question_id']
    return redirect(url_for('question_and_answers', question_id=question_id))


@app.route('/question/<answer_id>/vote_down')
def deduct_answer_rating(answer_id):
    answers = util.get_answers()
    listed_answer = util.get_data_by_id(answers, answer_id)
    answer_to_change = listed_answer[0]
    answer_to_change['vote_number'] -= 1
    question_id = answer_to_change['question_id']
    return redirect(url_for('question_and_answers', question_id=question_id))


if __name__ == '__main__':
    app.run()
