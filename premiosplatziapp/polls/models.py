from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish = models.DateTimeField("date of published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # not _id because the orm and automatically -> question_id
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
