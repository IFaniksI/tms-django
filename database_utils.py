# Напишите функцию populate_polls_database в файле database_utils.py.
# Функция должна принимать путь к json файлу с данными.
# Функция должна создавать и сохранять в базу данных объекты Question и Choice.
# (Опционально) Функция может предварительно очищать базу данных вопросов и ответов.
# Это может определяться параметром clean_database: bool.
# Проверьте выполнение функции в ./manage.py shell:
# >>> from database_utils import populate_polls_database
# >>> populate_polls_database('data.json', clean_database=True)

import json
from polls.models import Question, Choice
from django.utils import timezone


def populate_polls_database(path: str, clean_database: bool = False):

    with open(path, 'r') as file:
        data = json.load(file)

    if clean_database:
        Question.objects.all().delete()
        Choice.objects.all().delete()

    for question_text, choices in data.items():
        question = Question(question_text=question_text, pub_date=timezone.now())
        question.save()
        for choice_text, votes in choices.items():
            Choice(question=question, choice_text=choice_text, votes=votes)

