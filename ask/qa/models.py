from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')
    def popular(self):
        return self.order_by('-rating')   

class Question(models.Model):
    objects = QuestionManager()
    
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=False)
    likes = models.ManyToManyField(User, related_name='question_like_user',blank=True)

    def __unicode__(self):
        return self.title
    def get_url(self):
        return '/question/' + str(self.pk) + '/'

    class Meta:
        ordering = ('-id',)
   
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.text