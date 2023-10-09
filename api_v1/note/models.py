from django.db import models
from baseapp.models import BaseModel




class Category(models.Model):
     name  = models.CharField(max_length=300, verbose_name ="Kategoriya nomi")

     def __str__(self):
           return self.name


     class Meta:
          verbose_name  = "Kategoriya"


class Author(BaseModel):
     full_name = models.CharField(max_length=300, verbose_name="Ism sharifi")
     bio = models.TextField(verbose_name = "Author haqida malumot")
     number_book = models.IntegerField(default=0, verbose_name="Nechta kitob yozgan")


     def __str__(self):
          return self.full_name



class Book(BaseModel):
      name  = models.CharField(max_length=400, verbose_name = "Kitob nomi")
      description = models.TextField(verbose_name='kitob haqida')
      image = models.ImageField(upload_to='book/', blank=True, verbose_name="Kitobni rasmi")
      author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Kitobning Muallifi")
      category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")


      def __str__(self):
          return self.name


      class Meta:
          verbose_name = "Kitob"





