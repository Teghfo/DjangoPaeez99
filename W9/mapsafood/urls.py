from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from .views import index

from user_profile import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', index, name='home'),
    path('restaurant/', include('restaurant.urls')),
    path('profile/', include('user_profile.urls')),
    path('contact/', include('contact_admin.urls')),
    path('cart/', include('order.urls')),
    path('send_mail/', views.send_user_email),
]


if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
