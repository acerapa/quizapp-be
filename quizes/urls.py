from django.urls import path

from . import views

urlpatterns = [
    path('', views.quizes, name='create_quiz'),
    path('<int:quiz_id>/', views.quiz, name='quiz'),
    path('question/', views.questions, name='question' )
]
