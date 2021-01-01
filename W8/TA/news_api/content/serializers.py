from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, PrimaryKeyRelatedField, \
    SerializerMethodField, HyperlinkedIdentityField, CharField, IntegerField
from .models import News, Category
from user.serializers import CommentSerializer


class NewsListSerializer(HyperlinkedModelSerializer):
    # cat = PrimaryKeyRelatedField(read_only=True)
    # cat = SerializerMethodField()
    cat = CharField(source='cat.title')
    comments = CommentSerializer(source='comment_set', many=True)

    # def get_cat(self, instance):
    #     print(instance)
    #     return instance.cat.title

    class Meta:
        model = News
        fields = ('title', 'cat', 'url', 'comments')


class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
