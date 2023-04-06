from django.urls import path
from .api import *


urlpatterns = [
    path('answers/', AnswerListApi.as_view()),
    path('answers/<int:pk>/', AnswerDetailApi.as_view()),

    path('questions/', QuestionListApi.as_view()),
    path('questions/<int:pk>/', QuestionDetailApi.as_view()),

    path('exams/', ExamListApi.as_view()),
    path('exams/<int:pk>/', ExamDetailApi.as_view()),

    path('classrooms/', ClassRoomListApi.as_view()),
    path('classrooms/<int:pk>/', ClassRoomDetailApi.as_view()),

    path('accounts/', AccountListApi.as_view()),
    path('accounts/create/', CreateNewUser.as_view()),
    path('accounts/<int:pk>/', AccountDetailApi.as_view()),
]