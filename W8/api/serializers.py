from rest_framework import serializers

from .models import Book, Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'name']


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.Serializer):

    authors = AuthorSerializer(many=True, read_only=True)

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    publication = serializers.StringRelatedField()
    # authors = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='author-detail'
    # )

    # class Meta:
    #     model = Book
    #     fields = ['title', 'authors']
