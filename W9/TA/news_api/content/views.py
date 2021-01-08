from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import News, Category
from .serializers import NewsListSerializer, NewsDetailSerializer, CategorySerializer
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import NewsFilter

class NewsViewsSet(ReadOnlyModelViewSet):
    queryset = News.objects.all()
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = {'title': ['contains']}
    filterset_class = NewsFilter
    def get_serializer_class(self):

        serializers = {
            'list': NewsListSerializer,
            'retrieve': NewsDetailSerializer
        }
        # return serializers.get(self.action)
        print(serializers[self.action])
        return serializers[self.action]
        # if self.action == 'list':
        #     return NewsListSerializer
        # elif self.action == 'retrieve':
        #     return NewsDetailSerializer


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer




class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
