from django.urls import path
from .views import index, ProductListView

app_name = 'products'

urlpatterns = [
    path('index/', index, name='index'),
    path('<slug>/', ProductListView.as_view(), name='list'),
]
