from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # 설문조사 주제
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now-datetime.timedelta(days=1)

class Choice(models.Model):
    # Question Table의 id값 (주제참조)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 투표 선택지
    choice_text = models.CharField(max_length=200)
    # 투표 수
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
