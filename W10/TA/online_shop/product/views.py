from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, UpdateView, DetailView, CreateView
from django.http import HttpResponseNotFound


# Create your views here.

def ProductList(request):
    if request.method == 'GET':
        print('dddd')
        product_objects = Product.objects.all()
        product_objects_dict = {'product_objects': product_objects}
        return render(request, 'product/product_list1.html', context=product_objects_dict)


class ProductClassListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'product_objects'
    template_name = 'product/product_list1.html'

    def get_queryset(self):
        query_params = self.request.GET
        title_param = query_params.get('title', None)
        if title_param:
            queryset = Product.objects.filter(title=title_param)
        else:
            queryset = Product.objects.all()
        return queryset


def ProductDetail(request, product_id):
    if request.method == 'GET':
        try:
            product_object = Product.objects.get(id=product_id)
            product_object_dict = {'product_object': product_object}
        except:
            return HttpResponseNotFound('not found')

        return render(request, 'product/product_detail.html', context=product_object_dict)


class ProductClassDetailView(DetailView):
    model = Product
    context_object_name = 'product_object'
