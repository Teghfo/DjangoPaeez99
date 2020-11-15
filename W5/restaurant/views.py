from django.shortcuts import render, get_object_or_404

from .models import Category, Element


def element_list(request, cat_id, cat_title):
    category_obj = get_object_or_404(Category, id=cat_id)
    print(cat_title)
    elements = category_obj.element_set.all()
    # elements = Element.objects.filter(category=category_obj)

    context = {
        'category': category_obj,
        'elements': elements
    }
    return render(request, 'element-list.html', context)


def element_detail(request, elem_id):
    element = get_object_or_404(Element, id=elem_id)
    # elements = Element.objects.filter(category=category_obj)
    # addresses = element.address.all()
    context = {
        'element': element,
        # 'addresses': addresses
    }
    return render(request, 'element-detail.html', context)
