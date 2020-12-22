from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ba sen {self.age}"


class Publication(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
