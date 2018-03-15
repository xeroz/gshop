from django.urls import path
from .views import LoginTemplateView

app_name = 'products'

urlpatterns = [
    path('login/', LoginTemplateView.as_view(), name='login'),
    # path('product/<slug>/', ProductDetailView.as_view(), name='detail'),
]
