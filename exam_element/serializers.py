from rest_framework import serializers
from .models import StudentAnswer, Question, Exam, ClassRoom, Account



class StudentAnswerSerializer (serializers.ModelSerializer):

    class Meta :

        model = StudentAnswer
        fields = '__all__'



class QuestionSerializer (serializers.ModelSerializer):

    class Meta:

        model = Question
        fields = '__all__'



class ExamSerializer (serializers.ModelSerializer):

    class Meta:

        model = Exam
        fields = '__all__'



class ClassRoomSerializer (serializers.ModelSerializer):

    class Meta:

        model = ClassRoom
        fields = '__all__'



class AccountSerializer (serializers.ModelSerializer):

    class Meta:

        model = Account
        fields = '__all__'