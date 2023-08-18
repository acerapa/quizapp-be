from rest_framework import serializers

from .models import *

class QuizSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizSetting
        fields = ('id', 'quiz_id', 'participants', 'start_date', 'end_date', 'is_shuffle', 'is_active', 'participants_limit', 'deleted_at')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('quiz_id', 'description', 'choices', 'answer', 'deleted_at')

class QuizSerializer(serializers.ModelSerializer):
    quizsetting_set = QuizSettingSerializer(many=True, read_only=True)
    question_set = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ('id', 'title', 'instruction', 'created_by', 'deleted_at', 'quizsetting_set', 'question_set')

class QuizParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizParticipant
        fields = ('quiz_setting_id', 'user_id', 'is_active', 'deleted_at')
