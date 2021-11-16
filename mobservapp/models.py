from django.db import models

# Create your models here.
class mobmsg(models.Model):
    email=models.EmailField()
    msg=models.TextField()

