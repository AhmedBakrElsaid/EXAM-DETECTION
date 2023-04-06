from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *


class AnswerListApi(generics.ListCreateAPIView):
    serializer_class = StudentAnswerSerializer
    queryset = StudentAnswer.objects.all()
    permission_classes = [IsAuthenticated]


class AnswerDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentAnswerSerializer
    queryset = StudentAnswer.objects.all() 
    permission_classes = [IsAuthenticated]


class QuestionListApi(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]


class QuestionDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated] 


class ExamListApi(generics.ListCreateAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    permission_classes = [IsAuthenticated]


class ExamDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all() 
    permission_classes = [IsAuthenticated]


class ClassRoomListApi (generics.ListCreateAPIView):
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()
    permission_classes = [IsAuthenticated]


class ClassRoomDetailApi (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()
    permission_classes = [IsAuthenticated]


class AccountListApi (generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]


class AccountDetailApi (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]


class CreateNewUser(generics.CreateAPIView):
    serializer_class = CreateUserSerializer