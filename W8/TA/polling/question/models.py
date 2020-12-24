from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .files import File


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(max_length=100, upload_to=File.question_image, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey('Question', related_name='choices', related_query_name='choice',
                                 on_delete=models.CASCADE)
    text = models.CharField(max_length=30)
    choice_number = models.IntegerField()
    votes_number = models.IntegerField(default=0)

    class Meta:
        unique_together = ['question', 'choice_number']

    @property
    def counts(self):
        all_count = 0
        all_choices = self.question.choices.all()
        for choice in all_choices:
            all_count += choice.votes_number
        if all_count == 0:
            return 0
        return (float(self.votes_number) / all_count) * 100

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE)
    profile = models.ForeignKey('user.Profile', on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print('save')
        self.choice.votes_number += 1
        self.choice.save()
        return super().save()