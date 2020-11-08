from django.contrib import admin
from .models import Question, Category


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    raw_id_fields = ('cat',)


admin.site.register(Question, QuestionAdmin)

# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     raw_id_fields = ('cat',)


admin.site.register(Category)
