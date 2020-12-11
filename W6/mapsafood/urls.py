from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('__debug__/', include(debug_toolbar.urls)),
    path('', index, name='home'),
    path('restaurant/', include('restaurant.urls')),
    path('profile/', include('user_profile.urls')),
    path('contact/', include('contact_admin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
