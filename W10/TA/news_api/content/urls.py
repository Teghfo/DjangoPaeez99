from django.urls import path, include
from .views import NewsListView, NewsDetailView, CategoryView, NewsViewsSet
from rest_framework.routers import DefaultRouter, SimpleRouter

simple_router = SimpleRouter()
simple_router.register('news', NewsViewsSet)

urlpatterns = [
    path('news-list', NewsListView.as_view(), name='news-list'),
    path('news-detail/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('category', CategoryView.as_view(), name='category'),
    # path('', include(default_router.urls))
] + simple_router.urls