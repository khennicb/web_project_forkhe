from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible    # We need it because we use Python 2 
class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=6)
    def __str__(self):
        return self.name + "(#" + self.hex_code + ")"

@python_2_unicode_compatible    
class Square(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField(default=50)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + "x" + str(self.size)
    

    