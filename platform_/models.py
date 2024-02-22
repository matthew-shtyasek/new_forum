from django.contrib.auth.models import User
from django.db import models


class Partition(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Название')
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Название')
    partition = models.ForeignKey(Partition,
                                  on_delete=models.CASCADE,
                                  related_name='categories',
                                  verbose_name='Раздел')
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


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
    visible = models.BooleanField(default=False)

    @property
    def first_post(self) -> 'Post':
        return self.posts.order_by('-send_date').first()

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.body[:48]


class PostImage(models.Model):
    image = models.ImageField(upload_to='posts/%Y/%m/%d/')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='images')
    visible = models.BooleanField()

    def __str__(self):
        return self.image
