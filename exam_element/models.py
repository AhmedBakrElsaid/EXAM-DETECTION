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
    
    teacher_id = models.ManyToManyField(Account, related_name='teacher_id')




class Exam (models.Model):
    exam_id = models.ForeignKey(ClassRoom,related_name='exam_id',on_delete=models.CASCADE)



class StudentAnswer (models.Model):
    student_answer = models.ForeignKey('Question',related_name='student_answer',on_delete=models.SET_NULL,null=True,blank=True)
    answer = models.TextField()
    std_answer = models.ForeignKey(Account,related_name='std_answer',on_delete=models.CASCADE)
    




class Question (models.Model):
    questions = models.TextField()
    question_re = models.ForeignKey(Exam,related_name='question',on_delete=models.CASCADE)
    model_answer = models.TextField()
    
