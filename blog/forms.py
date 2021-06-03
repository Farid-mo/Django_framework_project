from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product


class ProductForm(UserCreationForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'user_id', 'tags_id', 'date_created']

        def __str__(self):
            return self.name


