from django.urls import path

from . import views

urlpatterns = [
    path('show_mall', views.show_mall, name='show-malls'),
    path('show_comment/<int:store_id>', views.comment, name='show-comments'),
    path('create-user', views.customer_create, name='create-user'),
    path('edit-user/<str:username>', views.customer_edit, name='edit-user'),
    path('delete-user/<str:username>', views.customer_delete, name='delete-user'),

]
