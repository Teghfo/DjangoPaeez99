from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200, blank=False)
    answer = models.IntegerField(default=1)
    option1 = models.CharField(max_length=40)
    option2 = models.CharField(max_length=40)
    option3 = models.CharField(max_length=40, blank=True)
    option4 = models.CharField(max_length=40, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)
