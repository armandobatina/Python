from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name_text = models.CharField(max_length=200)
    email_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('register date')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
