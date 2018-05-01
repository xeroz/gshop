from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ProfileTemplateView, create

app_name = 'users'

urlpatterns = [
    path('profile/', login_required(ProfileTemplateView.as_view()), name='profile'),
    path('create/', create, name='create'),
]
