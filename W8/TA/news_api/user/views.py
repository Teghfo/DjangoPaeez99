from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import RegisterSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from rest_framework.response import Response


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
