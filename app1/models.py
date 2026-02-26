from django.db import models

# Create your models here.

class book (models.Model):
    name =models.CharField (max_length=100)
    author=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    description=models.TextField()
    cover=models.ImageField(upload_to='covers/',null=True,blank=True)


    def __str__(self):
        return f"{self.name}"

