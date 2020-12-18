from django.urls import path, include

# from .views import element_list, element_detail, ElementList, ElementDetail


from .views import ElementDetail, ElementList, element_detail, SearchBox, ShowFood

urlpatterns = [
    path('element-list/<int:cat_id>/<str:cat_title>',
         ElementList.as_view(), name='element-list'),
    # path('element-detail/<int:pk>',
    #      ElementDetail.as_view(), name='element-detail'),

    path('element-detail/<int:elem_id>',
         element_detail, name='element-detail'),
    path('search/', SearchBox.as_view(), name='search'),
    path('show_food/', ShowFood.as_view(), name='show_food'),
]
