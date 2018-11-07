from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=400)
    pubdate = models.DateField()
    icon = models.ImageField(upload_to='images/')
    votes_total = models.CharField(default=1, max_length=50)
    url = models.URLField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100]
