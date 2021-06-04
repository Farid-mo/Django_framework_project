from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_posts, name='xxx'),
    path('home/', views.all_posts, name='xxx'),
    path('post/<str:pk>/', views.post, name='post'),

]
