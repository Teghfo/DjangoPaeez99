from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import authentication, permissions

from .models import Book, Author, Publication
from .serializers import BookSerializer, AuthorSerializer, AuthorDetailSerializer


@api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
def book_list(request):
    print(request.data.get('name'))
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorDetailView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name):
        try:
            author = Author.objects.get(name=name)
            serializer = AuthorDetailSerializer(author)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, name):
        try:
            author = Author.objects.get(name=name)
            serializer = AuthorDetailSerializer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': "update shod"})
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


class AuthorListGeneric(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request):
        print('in list')
        return super().list(request)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'name'
