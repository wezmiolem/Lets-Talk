from datetime import datetime
from collections import Counter
import mock_data


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


def get_data_by_id(listed_dicts, data_id):
    return [sentence for sentence in listed_dicts if sentence['id'] == int(data_id)]


def get_answers_for_question(question_id, answers):
    return [answer for answer in answers if answer['question_id'] == int(question_id)]


def get_new_id(listed_dicts):
    current_ids = [sentence['id'] for sentence in listed_dicts]
    return max(current_ids)+1


def get_current_datetime_string():
    now = datetime.now()
    date_time_str = now.strftime("%d/%m/%Y %H:%M:%S")
    return date_time_str


def add_to_data(listed_dicts, dict_data):
    listed_dicts.append(dict_data)


def num_of_answers_for_each_type(questions, answers):
    answer_types = [question['type'] for question in questions for answer in answers
                    if question['id'] == answer['question_id']]
    return Counter(answer_types)


def remove_from_data(listed_dicts, sentence_id):
    new_list = [sentence for sentence in listed_dicts if int(sentence_id) != sentence['id']]
    listed_dicts = new_list
