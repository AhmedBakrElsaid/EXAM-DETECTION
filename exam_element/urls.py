from django.urls import path
from .api import AnswerListApi , AnswerDetailApi, QuestionListApi, QuestionDetailApi, ExamListApi, ExamDetailApi, ClassRoomListApi, ClassRoomDetailApi, AccountListApi,AccountDetailApi



urlpatterns = [
    path('api/answers/all', AnswerListApi.as_view()),
    path('api/answer/<int:pk>', AnswerDetailApi.as_view()),


    path('api/question/all', QuestionListApi.as_view()),
    path('api/question/<int:pk>', QuestionDetailApi.as_view()),


    path('api/exam/all', ExamListApi.as_view()),
    path('api/exam/<int:pk>', ExamDetailApi.as_view()),


    path('api/classroom/all', ClassRoomListApi.as_view()),
    path('api/classroom/<int:pk>', ClassRoomDetailApi.as_view()),


    path('api/account/', AccountListApi.as_view()),
    path('api/account/<int:pk>', AccountDetailApi.as_view()),
]
