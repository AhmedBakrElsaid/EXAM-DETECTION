from django.urls import path
from .api import AnswerListApi , AnswerDetailApi, QuestionListApi, QuestionDetailApi, ExamListApi, ExamDetailApi, ClassRoomListApi, ClassRoomDetailApi, AccountListApi,AccountDetailApi



urlpatterns = [
    path('api/answer/', AnswerListApi.as_view()),
    path('api/answer/<int:pk>', AnswerDetailApi.as_view()),


    path('api/question/', QuestionListApi.as_view()),
    path('api/question/<int:pk>', QuestionDetailApi.as_view()),


    path('api/question/', ExamListApi.as_view()),
    path('api/question/<int:pk>', ExamDetailApi.as_view()),


    path('api/room/', ClassRoomListApi.as_view()),
    path('api/room/<int:pk>', ClassRoomDetailApi.as_view()),


    path('api/account/', AccountListApi.as_view()),
    path('api/account/<int:pk>', AccountDetailApi.as_view()),
]
