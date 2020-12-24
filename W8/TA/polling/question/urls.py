from django.urls import path
from .views import Home, QuestionList, QuestionDetail, QuestionResult, VoteQuestion, AddQuestion, AddChoice

urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('list', QuestionList.as_view(), name='question-list'),
    path('detail/<int:pk>', QuestionDetail.as_view(), name='question-detail'),
    path('detail/<int:pk>/result', QuestionResult.as_view(), name='question-result'),
    path('detail/<int:pk>/vote', VoteQuestion.as_view(), name='question-vote'),
    path('add_question/', AddQuestion.as_view(), name='question-add'),
    path('add_choice/', AddChoice.as_view(), name='choice-add'),
]
