from django.db import models
from django.template.defaultfilters import slugify

class Portfolio(models.Model):
    name_of_app = models.CharField(max_length=200)
    app_id = models.IntegerField(default=0)
    slogan = models.CharField(max_length=200, blank=True)
    short_description = models.CharField(max_length=200)
    date_finished= models.CharField(max_length=10)
    desc_achieved_1 = models.CharField(max_length=200, blank=True)
    desc_achieved_2 = models.CharField(max_length=200, blank=True)
    desc_achieved_3 = models.CharField(max_length=200, blank=True)
    desc_achieved_4 = models.CharField(max_length=200, blank=True)
    desc_achieved_5 = models.CharField(max_length=200, blank=True)
    desc_technical_1 = models.CharField(max_length=200, blank=True)
    desc_technical_2 = models.CharField(max_length=200, blank=True)
    desc_technical_3 = models.CharField(max_length=200, blank=True)
    desc_technical_4 = models.CharField(max_length=200, blank=True)
    desc_technical_5 = models.CharField(max_length=200, blank=True)
    tags_1 = models.CharField(max_length=20, blank=True)
    tags_2 = models.CharField(max_length=20, blank=True)
    tags_3 = models.CharField(max_length=20, blank=True)
    tags_4 = models.CharField(max_length=20, blank=True)
    tags_5 = models.CharField(max_length=20, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)

    # Unique URL slug for project
    slug = models.CharField(
        default="",
        max_length=30,
        unique=True)

    def __str__(self):
        return self.name_of_app 

    
