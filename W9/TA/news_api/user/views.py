from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import RegisterSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Comment
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet, ModelViewSet


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(approved=True)


class CommentView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        user = self.request.user
        comment_count = Comment.objects.filter(user=user).count()
        if comment_count >= 2:
            return Response(data={'detail': "not allowed"})
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED
from .serializers import PasswordSerializer, UserSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User


class SetPasswordViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(methods=['post'], url_name='name', url_path='set-pass', detail=False)
    def set_password(self, request):
        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        user = request.user
        if user.is_anonymous:
            return Response({'detail': 'you are not a user'})
        user.set_password(raw_password=validated_data['password'])
        user.save()
        return Response({'detail': 'you password succefully set'})

    # def update(self, request, *args, **kwargs):
    #     pass
    # def retrieve(self, request, *args, **kwargs):
    #     pass
    # def list(self):
    #     pass
    # def create(self):
    #     pass
    # def partial_update(self, request, *args, **kwargs):
    #     pass
    # def destroy(self, request, *args, **kwargs):
    #     pass

    def create(self, request):
        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        user = request.user
        if user.is_anonymous:
            return Response({'detail': 'you are not a user'})
        user.set_password(raw_password=validated_data['password'])
        return Response({'detail': 'you password succefully set'})
