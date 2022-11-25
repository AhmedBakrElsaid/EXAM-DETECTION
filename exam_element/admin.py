from django.contrib import admin
from .models import Account,Exam,Question,StudentAnswer,ClassRoom
# Register your models here.

admin.site.register(Account)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(StudentAnswer)
admin.site.register(ClassRoom)
