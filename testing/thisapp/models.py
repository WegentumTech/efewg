from django.db import models

# Create your models here.


class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    oneMore = models.CharField(max_length=50,default="wekf")
    again = models.CharField( max_length=50,default="wekf")
 
    def __str__(self):
        return self.title