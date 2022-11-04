from django.db import models
from django.urls import reverse
from django.utils import timezone


class Company(models.Model):
    title = models.TextField(verbose_name='title', null=True)
    jum_com = models.TextField(verbose_name='jum_com', null=True)
    jum_lang = models.TextField(verbose_name='jum_lang', null=True)
    jum_task = models.TextField(verbose_name='jum_task', null=True)
    jum_qlf = models.TextField(verbose_name='jum_qlf', null=True)
    jum_ter = models.TextField(verbose_name='jum_ter', null=True)
    jum_gift = models.TextField(verbose_name='jum_gift', null=True)
    jum_career = models.TextField(verbose_name='jum_career', null=True)
    jum_col = models.TextField(verbose_name='jum_col', null=True)
    jum_area = models.TextField(verbose_name='jum_area', null=True)

