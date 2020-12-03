import mock_data
from collections import Counter


def get_questions():
    return mock_data.questions


def get_question_headers():
    return mock_data.question_headers


def get_answers():
    return mock_data.answers


def get_question_types(questions):
    question_types = [question['type'] for question in questions]
    return Counter(question_types)


def get_questions_of_category(questions, category):
    if category == 'all':
        return questions
    return [question for question in questions if question['type'] == category]






