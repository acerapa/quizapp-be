from django.db import models

# Create a quiz model
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    instruction = models.TextField()
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

# Create a Quiz Setting model
class QuizSetting(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    is_shuffle = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    participants = models.ManyToManyField('users.User', through='QuizParticipant')
    participants_limit = models.IntegerField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

# Create a Quiz Participant model
class QuizParticipant(models.Model):
    quiz_setting_id = models.ForeignKey(QuizSetting, on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_passed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

# Create a Question model
class Question(models.Model):
    description = models.TextField()
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    choices = models.JSONField()
    answer = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
