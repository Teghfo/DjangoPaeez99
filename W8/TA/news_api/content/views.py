from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import News, Category
from .serializers import NewsListSerializer, NewsDetailSerializer, CategorySerializer


# Create your views here.


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
