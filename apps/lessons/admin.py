# django Core
from django.contrib import admin
# Owner
from .models import Lesson, TypeQuestion, Question, Answer, TakeLesson

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question')


@admin.register(TakeLesson)
class TakeLessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'lesson')


admin.site.register(Lesson)
admin.site.register(TypeQuestion)
admin.site.register(Question)


