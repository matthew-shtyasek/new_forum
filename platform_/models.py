from django.contrib.auth.models import User
from django.db import models


class Partition(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Название')


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Название')
    partition = models.ForeignKey(Partition,
                                  on_delete=models.CASCADE,
                                  related_name='categories',
                                  verbose_name='Раздел')


class Theme(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Название')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='themes',
                                 verbose_name='Категория')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='themes',
                               verbose_name='Автор')
    first_post = models.OneToOneField('Post',
                                      on_delete=models.CASCADE,
                                      related_name='themes',
                                      verbose_name='Первый пост')
    visible = models.BooleanField(default=False)


class Post(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор')
    theme = models.ForeignKey(Theme,
                              on_delete=models.CASCADE,
                              related_name='posts',
                              verbose_name='Тема')
    body = models.TextField(blank=False)
    send_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=False)
