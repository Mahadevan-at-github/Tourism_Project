from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)

class loginTable(models.Model):
    username = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    password2 = models.CharField(max_length=200,null=True)
    type = models.CharField(max_length=200)



    def __str__(self):
        return '{}'.format(self.username)


class Tourism(models.Model):

    PlaceName = models.CharField(max_length=200)
    Description = models.TextField()
    State = models.CharField(max_length=50)
    District = models.CharField(max_length=100)
    Weather_Choices = [
        ('SUNNY','Sunny'),
        ('RAINY','Rainy'),
        ('SNOWY','Snowy'),
    ]
    Weather = models.CharField(max_length=10,choices=Weather_Choices)
    Location_Link = models.URLField()
    Destination_Img = models.ImageField(upload_to='tourism_img/')
    Destination_Img1 = models.ImageField(upload_to='tourism_img/',blank=True,null=True)
    Destination_Img2 = models.ImageField(upload_to='tourism_img/',blank=True,null=True)
    Destination_Img3 = models.ImageField(upload_to='tourism_img/',blank=True,null=True)

    def __str__(self):
        return '{}'.format(self.PlaceName)