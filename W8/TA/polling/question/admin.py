from django.contrib import admin
from .models import Question, Choice


# Register your models here.

# admin.site.register(Question)
# admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    fields = ('text', 'choice_number')

#
# class ChoiceInline2(admin.StackedInline):
#     model = Choice
#     extra = 0
#     fields = ('text', 'choice_number')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('pk',)
#     inlines = [ChoiceInline]
