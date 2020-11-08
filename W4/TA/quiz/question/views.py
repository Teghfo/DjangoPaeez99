from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Question, Category


# Create your views here.


@csrf_exempt
def get_questions(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        output_list = []
        for item in categories:
            questions = item.question_set.all()[:5]
            for question in questions:
                output_list.append(
                    {'question_id': question.id, 'cat_name': item.name, 'cat_id': item.id,
                     'option1': question.option1, 'option2': question.option2, 'option3': question.option3,
                     'option4': question.option4})

        return JsonResponse(output_list, safe=False)
    else:
        return JsonResponse({'errors': 'you have not permission this method'}, safe=False)
