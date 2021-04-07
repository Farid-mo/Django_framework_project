from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tags'


class Product(models.Model):
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(default='', null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tags_id = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
