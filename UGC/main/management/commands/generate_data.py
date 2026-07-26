from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from ...models import Survey, Question, Answer
from user.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')

        survey_count = 2
        question_count = 15
        answer_count = 5

        self.stdout.write("Создание опросников")
        user = CustomUser.objects.get(id=1)
        for i in range(survey_count):
            survey = Survey.objects.create(name=fake.word(), author=user)

            for j in range(question_count):
                question = Question.objects.create(survey=survey, text=fake.sentence(nb_words=5) + '?', position=j + 1)

                answer_to_create = []
                for t in range(answer_count):
                    answer_to_create.append(Answer(question=question, text=fake.sentence(nb_words=2), position=t + 1))
                Answer.objects.bulk_create(answer_to_create)
