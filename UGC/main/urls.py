from django.urls import path

from .views import get_question

urlpatterns = [
    path("survey/<int:id_survey>/<int:num_question>/", get_question, name="question")
]
