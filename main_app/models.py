from django.db import models

# Create your models here.

class Wish(models.Model):
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.wish