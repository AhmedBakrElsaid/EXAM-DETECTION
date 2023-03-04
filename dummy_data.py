import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from exam_element.models import Account,ClassRoom,Question,StudentAnswer,Exam, User
import random
from faker import Faker


fake = Faker()

def seed_exam (n):
    for _ in range(n):
        name = fake.name()
        Exam.objects.create(
            name = name,
            teacher = Account.objects.get(id = random.randint(11 , 300)),
            classroom = ClassRoom.objects.get(id = random.randint(1 , 12)),
        )
    print(f"successfully {n} Exams")


def seed_question (n):
    for _ in range(n):
        model_answer = fake.text()
        question = fake.text()

        Question.objects.create(
            model_answer = model_answer,
            question = question,
            exam = Exam.objects.get(id = random.randint(1,20)),
        )
    print(f"successfully {n} questions")

def seed_classroom(n):
    for _ in range(n):
        name = fake.name()
        classroom = ClassRoom.objects.create(
            name = name,
            teacher_id = Account.objects.filter(account_type='Teacher').order_by('?').first(),
        )
        classroom.classrooms.add(Account.objects.get(id=random.randint(5,100)))
    print(f"successfully {n} rooms")


def seed_account(n):
    type_option = ['Teacher','Student']
    for _ in range(n):
        username = fake.name()
        password = fake.name()
        account_type = random.choice(type_option)
        Account.objects.create(
            user = User.objects.create(username=username, password=password),
            account_type = account_type,
            # classroom = ClassRoom.objects.get(id = random.randint(11,50)),
        )
    print(f"successfully {n} accounts")

def seed_stdanswer(n):
    for _ in range(n):
        answer = fake.text()
        StudentAnswer.objects.create(
            answer = answer,
            student = Account.objects.get(id=random.randint(11,250)),
            question = Question.objects.get(id=random.randint(11,250)),
            exam = Exam.objects.get(id = random.randint(1,20)),
        )
    print(f"successfully {n} stdans")


# seed_account(500)
# seed_classroom(50)
# seed_exam(20)
# seed_question(250)
seed_stdanswer(250)