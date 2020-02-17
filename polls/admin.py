from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2 # 디폴트 choice 갯수

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Title",{'fields': ['question_text']}),
        ("Date info",{'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
