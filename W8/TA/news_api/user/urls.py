from django.urls import path
from .views import RegisterView, CommentView, CommentListView, CommentUpdateView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('comment-add', CommentView.as_view(), name='comment-add'),
    path('comment-list', CommentListView.as_view(), name='comment-list'),
    path('comment-detail/<int:pk>', CommentUpdateView.as_view(), name='comment-detail'),
]
