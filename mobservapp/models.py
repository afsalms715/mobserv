from django.db import models

# Create your models here.
class mobmsg(models.Model):
    email=models.EmailField()
    msg=models.TextField()

class mobservices(models.Model):
    img=models.ImageField()
    heading=models.CharField(max_length=25)
    desc=models.TextField()


