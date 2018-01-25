from django.urls import path
from .views import index, ProductTemplateView

app_name = 'products'

urlpatterns = [
    path('index/', index, name='index'),
    path('categories/<slug>/', ProductTemplateView.as_view(), name='list'),
]
