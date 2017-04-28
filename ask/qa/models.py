from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"

Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа
"""

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    def __unicode__(self):
        return self.title

class QuestionManager(Question):
    def new(self):
        pass
    def popular(self):
        pass
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = ForeignKey(Question,on_delete=models.Cascade)
    author = models.ForeignKey(User,on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.text