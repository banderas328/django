from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=400)
    pubdate = models.DateField()


