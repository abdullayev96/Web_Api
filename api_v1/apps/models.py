from django.db import models

# Create your models here.


class Childern(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='image', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children')
    husband = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
