from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Question, Category
import json


# Create your views here.
@csrf_exempt
def get_questions(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        output_list = []
        for item in categories:
            questions = item.question_set.all().order_by('?')[:5]
            for question in questions:
                output_list.append(
                    {'question_id': question.id, 'cat_name': item.name, 'cat_id': item.id,
                     'option1': question.option1, 'option2': question.option2, 'option3': question.option3,
                     'option4': question.option4})

        return JsonResponse(output_list, safe=False)
    else:
        return JsonResponse({'errors': 'you have not permission this method'}, safe=False)


@csrf_exempt
def answer_questions(request):
    if request.method == 'POST':
        data = request.body
        question_answers = json.loads(data)
        score = Question.answer_questions(question_answers)
        return JsonResponse({'score:': '{:.2f}/100'.format(score)})