from django.shortcuts import render

from restaurant.models import Category
from django.utils.translation import gettext as _


def index(request):
    category = Category.objects.all().order_by('title')
    context = {
        'category': category,
        'name': 'ashkan'
    }
    print(_('category'))
    return render(request, 'index.html', context)
