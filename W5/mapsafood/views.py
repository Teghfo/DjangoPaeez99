from django.shortcuts import render

from restaurant.models import Category


def index(request):
    category = Category.objects.all()
    context = {
        'category': category,
        'name': 'ashkan'
    }
    return render(request, 'index.html', context)
