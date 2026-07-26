import datetime

from django.db import models

from user.models import CustomUser


class Survey(models.Model):
    name = models.CharField(max_length=100, blank=False, db_index=True, verbose_name="Название опроса")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="surveys",
                               verbose_name="Автор опроса")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Опросник"
        verbose_name_plural = "Опросники"

    def __str__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions", verbose_name="Опрос")
    text = models.TextField(blank=False, verbose_name="Содержание вопроса")
    position = models.PositiveIntegerField(verbose_name="Номер вопроса")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers", verbose_name="Ответ")
    text = models.TextField(blank=False, verbose_name="Содержание ответа")
    position = models.PositiveIntegerField(verbose_name="Позиция ответа")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.text


class Statistic(models.Model):
    # Можно добавить любое поле, по которому хотим считать статистику
    # Для примеры приведены поля времени прохождения и количества ответов ( с учтом что вопрос можно пропустить и не отвечать)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="statistic", verbose_name="Опросник")
    completion_time = models.DurationField(verbose_name="Время прохождения", default=datetime.timedelta(0))
    count_answer = models.PositiveIntegerField(blank=False, default=0, verbose_name="Количество ответов")
