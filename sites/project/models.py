from django.db import models
from django.contrib.auth.models import User



class  Category(models.Model):
    name = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logo  = models.ImageField(upload_to='book')
    title = models.CharField(max_length=400)
    subtitle = models.CharField(max_length=200)
    desc = models.TextField()
    type = models.CharField(max_length=100)
    version = models.CharField(max_length=300)
    size = models.CharField(max_length=300)
    os = models.FloatField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    advantage = models.CharField(max_length=400)
    category  = models.ForeignKey("Category", on_delete=models.CASCADE)
    downland = models.URLField(max_length=4000)
    url_name = models.URLField(max_length=2000)
    screen = models.ImageField(upload_to='images/')
    screen1 = models.ImageField(upload_to='good/')
    screen2 = models.ImageField(upload_to='cool/')
    likes = models.PositiveBigIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



