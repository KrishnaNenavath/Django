from django.db import models

# Create your models here.

class Courses(models.Model):
    image = models.ImageField(upload_to='images/')
    summary= models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.summary