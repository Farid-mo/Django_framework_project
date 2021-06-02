from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.all_posts, name='xxx'),

]
