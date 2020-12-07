from django.urls import path
from .views import ProductList, ProductClassListView, ProductDetail, ProductClassDetailView

urlpatterns = [
    path('product_list/', ProductList, name='product-list'),
    path('product_class_list/', ProductClassListView.as_view(), name='product-class-list'),
    path('product_detail/<int:product_id>/', ProductDetail, name='product-class-list'),
    path('product_class_detail/<int:pk>/', ProductClassDetailView.as_view(), name='product-class-detail'),
]
