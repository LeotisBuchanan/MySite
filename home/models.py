import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_txt = models.CharField(max_length=300)
    pub_date = models.DateTimeField("Date Published")

    def __unicode__(self):
        return self.question_txt

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    list_display = (question_txt, pub_date, was_published_recently)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_txt = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_txt

class PageViews(models.Model):
    no_views = models.IntegerField(default=0)

    def __unicode__(self):
        return 'No of views'

