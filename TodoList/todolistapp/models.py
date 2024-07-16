from django.db import models

# Create your models here.

class Todolist(models.Model):
    text = models.CharField(max_length=45)
    comlited = models.BooleanField(default = False)

    def __self__(self):
        return self.text