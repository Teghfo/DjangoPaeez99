from rest_framework import serializers

from .models import Book, Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'name', 'age']
        extra_kwargs = {
            'url': {'view_name': 'author-information', 'lookup_field': 'name'}, }


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        print("in update", instance.age)
        return super().update(instance, validated_data)

    def to_internal_value(self, data):
        age = int(data.get('age', 0))
        print(age)
        if age:
            if age < 20:
                raise serializers.ValidationError({
                    'age': 'Boro Bozorg sho.'})
        else:
            raise serializers.ValidationError({
                'age': 'in lazemeh.'})

        return super().to_internal_value(data)


class BookSerializer(serializers.Serializer):

    # authors = AuthorSerializer(many=True, read_only=True)

    id = serializers.IntegerField(read_only=True)
    book_name = serializers.CharField(source="title", max_length=50)
    publication = serializers.StringRelatedField()
    authors = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='author-information',
        lookup_field='name',
    )

    owner_publication = serializers.SerializerMethodField()

    def get_owner_publication(self, obj):
        return obj.publication.owner.aghazadeh

    def to_representation(self, obj):
        ret = super().to_representation(obj)
        ret['test'] = 'ashkan'
        return ret

    # class Meta:
    #     model = Book
    #     fields = ['title', 'authors']


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['title', 'authors', 'publication']
#         depth = 2
