from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ProfileTemplateView, create, WishListTemplateView

app_name = 'users'

urlpatterns = [
    path('profile/', login_required(ProfileTemplateView.as_view()), name='profile'),
    path('wish_list/', login_required(WishListTemplateView.as_view()), name='wish_list'),
    path('create/', create, name='create'),
]
