from django.contrib import admin
from .models import User, Exam, Question, StudentAnswer, ClassRoom
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(StudentAnswer)
admin.site.register(ClassRoom)
