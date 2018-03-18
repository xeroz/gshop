from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ProfileTemplateView

app_name = 'products'

urlpatterns = [
    path('profile/', login_required(ProfileTemplateView.as_view()), name='profile'),
]
