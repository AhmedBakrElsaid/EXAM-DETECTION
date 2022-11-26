from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TYPE_OPTION =(
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
)



class Account(models.Model) :
    
    user = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50,choices=TYPE_OPTION)
    student_id = models.ForeignKey('ClassRoom',related_name='student_id',on_delete=models.CASCADE)




class ClassRoom (models.Model):
    
    teacher_id = models.ManyToManyField(Account, related_name='teacher_id', on_delete = models.SET_NULL,blank=True,null=True)




class Exam (models.Model):
    exam_id = models.ForeignKey(ClassRoom,related_name='exam_id',on_delete=models.CASCADE)



class StudentAnswer (models.Model):
    pass




class Question (models.Model):
    question = models.ForeignKey(Exam,related_name='question',on_delete=models.CASCADE)
