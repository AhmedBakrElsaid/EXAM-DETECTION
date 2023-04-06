from django.db import models
from django.contrib.auth.models import AbstractUser


TYPE_OPTION =(
    ('teacher', 'teacher'),
    ('student', 'student'),
)

class User(AbstractUser) :
    account_type = models.CharField(max_length=50, choices=TYPE_OPTION)
    password = models.CharField(max_length=50) 		
    # classroom = models.ForeignKey('ClassRoom', related_name='student_id', on_delete=models.CASCADE)
    classroom = models.ManyToManyField('ClassRoom', related_name='classrooms', blank=True)

    def __str__(self) -> str:
        return self.username


class ClassRoom(models.Model):
    # add validator it is a teacher who created the classroom
    teacher_id = models.OneToOneField(User, related_name='teacher_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='classroom')

    def __str__(self) -> str:
        return self.name


class Exam(models.Model):
    name= models.CharField(max_length=255, default='classroom')
    exam_code = models.CharField(max_length=255, default='#0000', blank=True, null=True)
    teacher = models.ForeignKey(User, related_name="exams", on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, related_name='classroom', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)
    question = models.TextField()
    model_answer = models.TextField()

    def __str__(self) -> str:
        return self.question


class StudentAnswer(models.Model):
    student = models.ForeignKey(User, related_name='std_answer', on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, related_name='exam_answers', on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey('Question', related_name='student_answer', on_delete=models.SET_NULL, null=True, blank=True)
    grade = models.CharField(max_length=255, default='0', blank=True, null=True)
    answer = models.TextField()

    def __str__(self) -> str:
        return self.answer
    