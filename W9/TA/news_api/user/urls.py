from django.urls import path
from .views import RegisterView, CommentView, CommentListView, CommentUpdateView, SetPasswordViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

simple_router = SimpleRouter()
simple_router.register('password-root-api', SetPasswordViewSet, basename='set-pass')


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('comment-add', CommentView.as_view(), name='comment-add'),
    path('comment-list', CommentListView.as_view(), name='comment-list'),
    path('comment-detail/<int:pk>', CommentUpdateView.as_view(), name='comment-detail'),
] + simple_router.urls
