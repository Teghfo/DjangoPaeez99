from django.urls import path


from .views import book_list, AuthorDetailView, AuthorListView


urlpatterns = [
    path('book_list/', book_list, name="book_list"),
    path('author_detail/<int:pk>', AuthorDetailView.as_view(), name="author-detail"),
    path('author_list/', AuthorListView.as_view(), name="author-list"),
]
