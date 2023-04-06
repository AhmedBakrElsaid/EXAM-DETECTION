from rest_framework import serializers
from .models import StudentAnswer, Question, Exam, ClassRoom, User


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'account_type']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password',  'account_type']
        extra_kwargs = {"password":{'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user    