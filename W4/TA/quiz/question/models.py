from django.db import models

from random import choice, randint, shuffle


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200, blank=False)
    answer = models.IntegerField(default=1)
    option1 = models.CharField(max_length=40)
    option2 = models.CharField(max_length=40)
    option3 = models.CharField(max_length=40, blank=True)
    option4 = models.CharField(max_length=40, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    positive_score = 3
    negative_score = -1

    def __str__(self):
        return str(self.id)

    @classmethod
    def generate_questions(cls):
        options = ["salam", "khoobi", "chetori", "khoobam"]
        cats = Category.objects.all()
        for i in range(80):
            random_choice = randint(1, 4)
            shuffle(options)
            dict_fields = {
                "title": "کدام یک از گزینه های زیر درست است؟",
                "answer": random_choice,
                "option1": options[0],
                "option2": options[1],
                "option3": options[2],
                "option4": options[3],
                "cat": choice(cats)
            }
            cls.objects.create(**dict_fields)

    @classmethod
    def answer_questions(cls, question_answers):
        question_count = 20
        score = 0
        print(question_answers)
        for question_id, answer in question_answers.items():
            try:
                real_answer = Question.objects.get(id=question_id).answer
                user_answer = answer
                if real_answer == user_answer:
                    score += cls.positive_score
                elif real_answer != user_answer:
                    score += cls.negative_score
            except Question.DoesNotExist:
                continue
        real_score = score / (question_count * 3) * 100
        return real_score


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)

    @classmethod
    def generate_cat(cls):
        cat = ['سینما', 'ورزشی', 'سیاسی', 'هنری']
        for cat_name in cat:
            cls.objects.get_or_create(name=cat_name)
