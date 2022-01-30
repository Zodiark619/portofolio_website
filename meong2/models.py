from django.db import models

# Create your models here.
class expansion(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class faction(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class type(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class waifu(models.Model):
    name=models.CharField(max_length=200)
    
    faction=models.ForeignKey(faction,on_delete=models.CASCADE,related_name='bolo2_faction')

    expansion=models.ForeignKey(expansion,on_delete=models.CASCADE,related_name='bolo_expansion')
    type=models.ManyToManyField(type,related_name='bolo1_type')

    def __str__(self):
        return f"{self.name} + {self.expansion}"