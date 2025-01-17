from django.contrib import admin
from .models import Question, Choice

class Choiceinline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    filedsets = [
        (None, {
            "fields":["Question_text"]
        }),
        ('Date Information', {"fields": ['pub_date'], 'classes': ['collapse']})
    ]
    inlines =[Choiceinline]
    list_display= ('question_text', 'pub_date')
    list_filter= ('pub_date')
    search_fields =['question_text']
    
admin.site.register(Question)
admin.site.register(Choice)