from django.forms import Form, IntegerField, ModelForm
from .models import Choice, Question


class AnswerForm(Form):
    answer_number = IntegerField()


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_number', 'text', 'question')


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('title',)