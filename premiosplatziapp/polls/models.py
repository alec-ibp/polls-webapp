import datetime

from django.utils import timezone
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish = models.DateTimeField("date of published")


    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.publish >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # not _id because the orm add automatically -> question_id
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self) -> str:
        return f"{self.choice_text} votes: {self.votes}"
