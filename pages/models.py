from django.db import models

class Pages(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)       

    def __str__(self):
        return self.name   


