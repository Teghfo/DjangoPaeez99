from django.urls import path, include


from .views import book_list, AuthorDetailView, AuthorListView, AuthorListGeneric, AuthorViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('adel_danaey', AuthorViewSet, basename='author')


urlpatterns = [
    path('book_list/', book_list, name="book_list"),
    path('author_detail/<str:name>', AuthorViewSet.as_view({"get": "retrieve"}),
         name="author-information"),
    path('author_list/',
         AuthorViewSet.as_view({"get": "list"}), name="author-list"),
    path('', include(router.urls))
]
