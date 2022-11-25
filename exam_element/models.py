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




class ClassRoom (models.Model):
    pass



class Exam (models.Model):
    pass



class StudentAnswer (models.Model):
    pass




class Question (models.Model):
    pass
