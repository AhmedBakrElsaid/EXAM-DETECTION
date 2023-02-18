from django.db import models
from django.contrib.auth.models import User

TYPE_OPTION =(
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
)

class Account(models.Model) :
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50, choices=TYPE_OPTION)
    # classroom = models.ForeignKey('ClassRoom', related_name='student_id', on_delete=models.CASCADE)
    classroom = models.ManyToManyField('ClassRoom', related_name='classrooms', blank=True)

    def __str__(self) -> str:
        return self.user.username



class ClassRoom(models.Model):
    # add validator it is a teacher who created the classroom
    teacher_id = models.OneToOneField(Account, related_name='teacher_id', on_delete=models.CASCADE)
    name= models.CharField(max_length=255, default='classroom')

    def __str__(self) -> str:
        return self.name




class Exam(models.Model):
    teacher = models.ForeignKey(Account, related_name="exams", on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, related_name='classroom', on_delete=models.CASCADE)
    name= models.CharField(max_length=255, default='classroom')

    def __str__(self) -> str:
        return self.name




class Question(models.Model):
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)
    question = models.TextField()
    model_answer = models.TextField()

    def __str__(self) -> str:
        return self.question





class StudentAnswer(models.Model):
    student = models.ForeignKey(Account, related_name='std_answer', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', related_name='student_answer', on_delete=models.SET_NULL, null=True, blank=True)
    answer = models.TextField()

    def __str__(self) -> str:
        return self.answer
    