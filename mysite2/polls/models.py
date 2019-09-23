import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return timezone.now() > self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Suggestion(models.Model):
    sug_name = models.CharField(max_length=150)
    body_text = models.TextField(max_length=1500)
    sub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.body_text





