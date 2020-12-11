from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView

from .models import Category, Element, Food, ElementAddress


# -------------------- Functional Base View

# def element_list(request, cat_id, cat_title):
#     category_obj = get_object_or_404(Category, id=cat_id)
#     print(cat_title)
#     elements = category_obj.element_set.all()
#     # elements = Element.objects.filter(category=category_obj)

#     context = {
#         'category': category_obj,
#         'elements': elements
#     }
#     return render(request, 'element-list.html', context)


def element_detail(request, elem_id):
    element = get_object_or_404(Element, id=elem_id)
    # elements = Element.objects.filter(category=category_obj)
    # addresses = element.address.all()
    context = {
        'element': element,
        'price': 64679646464767
        # 'addresses': addresses
    }
    return render(request, 'element-detail.html', context)


# ---------------------- Class Base View

# class ElementList(View):

#     def get(self, request, cat_id, cat_title, *args, **kwarg):
#         category_obj = get_object_or_404(Category, id=cat_id)
#         print(cat_title)
#         elements = category_obj.element_set.all()
#         # elements = Element.objects.filter(category=category_obj)

#         context = {
#             'category': category_obj,
#             'elements': elements
#         }
#         return render(request, 'element-list.html', context)

#     def post(self, request, *args, **kwarg):
#         return JsonResponse({"status": "class base view"})


# class ElementDetail(TemplateView):
#     template_name = 'element-detail.html'

#     def get_context_data(self, elem_id, **kwargs):
#         context = super().get_context_data(**kwargs)
#         element = get_object_or_404(Element, id=elem_id)
#         context['element'] = element
#         return context


# ------------------- Generic View

class ElementList(ListView):
    model = Element
    template_name = 'element-list.html'
    context_object_name = 'elements'
    paginate_by = 1

    def get_queryset(self):
        cat_id = self.kwargs['cat_id']
        cat_title = self.kwargs['cat_title']
        category_obj = get_object_or_404(Category, id=cat_id)
        elements = category_obj.element_set.all()
        # elements = Element.objects.filter(category=category_obj)
        return elements
        # return super().get_queryset(*args)


class ElementDetail(DetailView):
    model = Element
    template_name = 'element-detail.html'

    # def get_object(self):
    #     element = get_object_or_404(Element, id=self.kwargs['elem_id'])
    #     return element


# custom class View
# class CustomView(View):
#     template_name = None
#     queryset = None
#     model = None
#     object_name = 'object_list'

#     def __init__(self):
#         if not self.queryset:
#             self.queryset = self.get_queryset()
#         if not self.template_name:
#             self.template_name = self.model._meta.model_name '.html'
#
#     def get_queryset(self):
#         return self.model.objects.all()

#     def get(self, request, cat_id, cat_title):

#         context = {
#             self.object_name: self.queryset
#         }

#         return render(request, self.template_name, context)


# class ElementList(CustomView):
#     model = Element
#     template_name = 'element-list.html'
#     object_name = 'elements'
#     queryset = Element.objects.all()


# ToDo panjshanbe
class SearchBox(View):
    def get(self, request):
        query_set = Food.objects.all()
        if request.GET.get('res_name'):
            query_set = query_set.filter(
                cat_manu__element__name__contains=request.GET.get('res_name'))
        if request.GET.get('street_name'):
            query_set = query_set.filter(
                cat_manu__element__address__street__contains=request.GET.get('street_name'))
        if request.GET.get('city_name'):
            query_set = query_set.filter(
                cat_manu__element__address__city=request.GET.get('city_name'))
        if request.GET.get('food_name'):
            query_set = query_set.filter(
                name__contains=request.GET.get('food_name'))

        print(query_set)
        response = HttpResponse("ok shod")
        response.set_cookie('name', 'ashkan', max_age=30)
        return response
        # foods = Food.objects.filter(cat_manu__element__)
        # foods_address = ElementAddress.objects.select_related('element').filter(
        #     city=request.GET.get('city'), street=request.GET.get('street'))

        # element_list = []
        # for elem in foods_address:
        #     element_list.append(elem.element.filter(
        #         name=request.GET['restaurant_name']))
        # food_list = []
        # for elem in element_list:
        #     for obj in elem:
        #         if request.GET.get('street') and obj.name=request.GET.get('street')
        #             if
