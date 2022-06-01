from turtle import title
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    date_pub = models.DateField((""), auto_now=True)
    date_up = models.DateField((""), auto_now_add=True)
    text = models.TextField()