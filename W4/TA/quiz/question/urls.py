from django.urls import path

from .views import get_questions, answer_questions

urlpatterns = [
    path('questions_list/', get_questions),
    path('answer/', answer_questions),
]
