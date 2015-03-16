from django.db import models

# Create your models here.
class Posts(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    body_text = models.TextField()
    pub_date = models.DateTimeField('Date Published')

    def __unicode__(self):
        return self.title
