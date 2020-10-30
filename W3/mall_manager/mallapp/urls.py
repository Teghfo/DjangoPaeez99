from django.urls import path

from .views import show_mall, comment

urlpatterns = [
    path('show_mall', show_mall),
    path('show_comment/<int:store_id>', comment),

]
