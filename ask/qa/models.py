from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='question_like_user',blank=True)
    def __unicode__(self):
        return self.title

class QuestionManager(models.Manager):
    def new(self):
        from django.db import connection
        cursor = connection.cursor()
    def popular(self):
        from django.db import connection
        cursor = connection.cursor()    
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    def __unicode__(self):
        return self.text