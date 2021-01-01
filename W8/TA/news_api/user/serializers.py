from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer, CharField
from .models import Comment


# Create your views here.


class RegisterSerializer(ModelSerializer):
    token = CharField(read_only=True)
    username = CharField(write_only=True)
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'token')

    def create(self, validated_data):
        user = super().create(validated_data)
        token = Token.objects.create(user=user)
        self.token = token.key
        return user

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        print(rep)
        rep['token'] = self.token
        return rep


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'news')
