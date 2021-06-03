from django.urls import path
from . import views
from .views import UserEditView

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('edit', UserEditView.as_view(), name='profile_edit'),
    path('form', views.profile_user, name='prof_form'),



]
