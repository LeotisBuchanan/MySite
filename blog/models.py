from django.db import models

from ckeditor.fields import RichTextField

class Posts(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    body_text = RichTextField()
    pub_date = models.DateTimeField('Date Published')

    def __unicode__(self):
        return self.title
