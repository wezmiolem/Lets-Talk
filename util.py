from datetime import datetime

import mock_data
from collections import Counter


def get_questions():
    return mock_data.questions


def get_question_headers():
    return mock_data.question_headers


def get_answers():
    return mock_data.answers


def get_question_keys():
    return mock_data.question_keys


def get_answer_keys():
    return mock_data.answer_keys


def get_question_types(questions):
    question_types = [question['type'] for question in questions]
    return Counter(question_types)


def get_questions_of_category(questions, category):
    if category == 'all':
        return questions
    return [question for question in questions if question['type'] == category]


def get_question_by_id(questions, question_id):
    return [question for question in questions if question['id'] == int(question_id)]


def get_answers_for_question(question_id, answers):
    return [answer for answer in answers if answer['question_id'] == int(question_id)]


def get_new_id(listed_dicts):
    current_ids = [sentence['id'] for sentence in listed_dicts]
    return max(current_ids)+1


def get_current_datetime_string():
    now = datetime.now()
    date_time_str = now.strftime("%d/%m/%Y %H:%M:%S")
    return date_time_str



def add_to_data(listed_dicts, question):
    listed_dicts.append(question)








