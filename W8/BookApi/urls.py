
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustumObtainToken(views.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if not created:
            token.delete()
            token = Token.objects.create(user=user)
        return Response({'token': token.key})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-token-auth/', CustumObtainToken.as_view()),

]

# "token": "acf6517c515b86ecc9ed2b096b8eaaa2b1669874"
