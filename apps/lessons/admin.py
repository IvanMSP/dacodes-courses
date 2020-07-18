# django Core
from django.contrib import admin
# Owner
from .models import Lesson, TypeQuestion, Question, Answer

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question')


admin.site.register(Lesson)
admin.site.register(TypeQuestion)
admin.site.register(Question)


