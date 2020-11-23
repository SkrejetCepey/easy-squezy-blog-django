from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        pass

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)))
        return reverse('home')
        pass

    pass


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    # title_tag = models.CharField(max_length=255, default="TestBlog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='unstated')

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
        pass

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)))
        return reverse('home')
        pass

    pass
