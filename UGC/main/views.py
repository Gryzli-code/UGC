from django.shortcuts import render
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Survey, Question, Answer


def get_question(request, id_survey, num_question):
    survey_db = get_object_or_404(Survey, id=id_survey)
    question = Question.objects.prefetch_related(
        Prefetch("answers", queryset=Answer.objects.order_by('position'))).get(survey=survey_db, position=num_question)
    question_data = model_to_dict(question, fields=["id", "text"])
    question_data["answers"] = [model_to_dict(answer, fields=["id", "text"]) for answer in question.answers.all()]

    return JsonResponse({'status': '200', "question": question_data})
