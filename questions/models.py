from django.db import models


class Question(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question)
    user = models.CharField(max_length=100)
    text = models.TextField()

    def __unicode__(self):
        return self.text
