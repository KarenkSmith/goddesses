from django.db import models

# Create your models here.
class God(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    use_for = models.TextField(max_length=100)


def __str__ (self):
    return self.name