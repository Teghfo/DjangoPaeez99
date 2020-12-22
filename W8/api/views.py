from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Book, Author, Publication
from .serializers import BookSerializer, AuthorSerializer, AuthorDetailSerializer


@api_view(['GET', 'POST'])
def book_list(request):
    print(request)
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorDetailView(APIView):
    def get(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorDetailSerializer(author)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AuthorListView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serilizer = AuthorSerializer(
            authors, many=True, context={'request': request})
        return Response(serilizer.data)

    def post(self, request):
        serializer = AuthorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
