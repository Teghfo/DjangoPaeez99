from django.urls import path
from .views import NewsListView, NewsDetailView, CategoryView

urlpatterns = [
    path('news-list', NewsListView.as_view(), name='news-list'),
    path('news-detail/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('category', CategoryView.as_view(), name='category')
]
