from django.db import models
from django.urls import reverse
from django.utils import timezone


class Opensource(models.Model):
    pro_nm = models.TextField(verbose_name='pro_nm', null=True)
    stars = models.IntegerField('stars', null=True)
    forks = models.IntegerField('forks', null=True)
    git_license = models.TextField('git_license', null=True)
    update = models.DateTimeField('update', auto_now=True)
    create = models.DateTimeField('create', default=timezone.now)
    lang = models.TextField('lang', null=True)
    topic = models.TextField('topic', null=True)

