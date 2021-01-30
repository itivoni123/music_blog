from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Post(models.Model):

    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    categories = models.CharField(max_length=255, default='music')
    likes = models.ManyToManyField(User, related_name='music_blog')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):

        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')
