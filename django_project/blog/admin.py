from django.contrib import admin
from .models import Quizz, Question, Choice, Answer

admin.site.register(Quizz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
