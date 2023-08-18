from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import QuizSerializer, QuizSettingSerializer, QuestionSerializer

from .models import Quiz, QuizSetting, Question


@api_view(['POST', 'GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def quizes(request):
    quiz = None
    quiz_setting = None

    if request.method == 'POST':
        quizSerializer = QuizSerializer(data=request.data['quiz'])
        quiz_setting_data = request.data['setting']

        if quizSerializer.is_valid():
            quiz = quizSerializer.save()

            quiz_setting_data['quiz_id'] = quiz.id
            quizSettingSerializer = QuizSettingSerializer(data=quiz_setting_data)
            if quizSettingSerializer.is_valid():
                quiz_setting = quizSettingSerializer.save()
            else:
                return Response(quizSettingSerializer.errors, status=400)
        else:
            return Response(quizSerializer.errors, status=400)

        data = {
            'quiz': QuizSerializer(quiz).data,
            'setting': QuizSettingSerializer(quiz_setting).data
        }

    elif request.method == 'GET':
        quizes = Quiz.objects.filter(
            created_by=request.user.id,
            deleted_at__isnull=True
        )

        quizSerializer = QuizSerializer(quizes, many=True)

        data = {
            'quizes': quizSerializer.data
        }

    return Response(data, status=200)

@api_view(['GET', 'PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def quiz(request, quiz_id):
    data = {}
    if request.method == 'PUT':
        try:
            quiz = Quiz.objects.get(id=quiz_id)
            quiz_setting = QuizSetting.objects.get(quiz_id=quiz.id)
        except Quiz.DoesNotExist:
            return Response(status=404)
        
        quizSerializer = QuizSerializer(quiz, data=request.data['quiz'])
        if quizSerializer.is_valid():
            quizSerializer.save()

            setting = request.data['setting']
            setting['quiz_id'] = quiz.id
            quizSettingSerializer = QuizSettingSerializer(quiz_setting, data=setting)
            if quizSettingSerializer.is_valid():
                quizSettingSerializer.save()

                data = {
                    'update': True
                }
            else:
                return Response(quizSettingSerializer.errors, status=400)
        else:
            return Response(quizSerializer.errors, status=400)
        
    elif request.method == 'GET':
        quiz = Quiz.objects.get(id=quiz_id)
        
        data = {
            'quiz': QuizSerializer(quiz).data
        }

    return Response(data, status=200)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def questions(request):
    questionSerializer = QuestionSerializer(request.data)

    if questionSerializer.is_valid():
        question = questionSerializer.save()
        return Response({'success': True}, status=200)
    else:
        Response(questionSerializer.errors, status=400)
