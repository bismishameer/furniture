from django.db import models


class fur(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pic')
    desc=models.TextField()

    def __str__(self):
        return self.name

