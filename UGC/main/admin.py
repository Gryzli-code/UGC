from django.contrib import admin

from .models import Question, Answer


@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ("survey", "text", "position",)
    list_editable = ("position",)
    list_per_page = 15


@admin.register(Answer)
class Answer(admin.ModelAdmin):
    list_display = ("question", "text", "position",)
    list_editable = ("position",)
    list_per_page = 30
