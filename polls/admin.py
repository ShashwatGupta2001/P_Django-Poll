from django.contrib import admin

# Register your models here.

# Adding Questions:

from .models import Question

# M1
# # admin.site.register(Question)

# M2
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# admin.site.register(Question, QuestionAdmin)

# M3
# Splitting the two field choices
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

# admin.site.register(Question, QuestionAdmin)

# Adding Choices:

# M1
from .models import Choice
# admin.site.register(Choice)

# M2
class ChoiceInline(admin.TabularInline): # TabularInline uses less space on screen
#class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']

    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)