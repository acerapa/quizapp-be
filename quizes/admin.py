from django.contrib import admin
from .models import Quiz, QuizSetting, Question

# Register your models here.
admin.site.register(Question)
admin.site.register(QuizSetting)
admin.site.register(Quiz)