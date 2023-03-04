from rest_framework import generics
from .serializers import StudentAnswerSerializer, QuestionSerializer, ExamSerializer, ClassRoomSerializer, AccountSerializer
from .models import StudentAnswer, Question, Exam, ClassRoom, Account


class AnswerListApi(generics.ListCreateAPIView):
    serializer_class = StudentAnswerSerializer
    queryset = StudentAnswer.objects.all()


class AnswerDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentAnswerSerializer
    queryset = StudentAnswer.objects.all() #wrong fix it


class QuestionListApi(generics.ListCreateAPIView):
    
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionDetailApi(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = QuestionSerializer
    queryset = Question.objects.all() # wrong fix it


class ExamListApi(generics.ListCreateAPIView):
    
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class ExamDetailApi(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = ExamSerializer
    queryset = Exam.objects.all() # wrong fix it


class ClassRoomListApi (generics.ListCreateAPIView):
    
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()


class ClassRoomDetailApi (generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()# wrong fix it


class AccountListApi (generics.ListCreateAPIView):
    
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountDetailApi (generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = AccountSerializer
    queryset = Account.objects.all()# wrong fix it
