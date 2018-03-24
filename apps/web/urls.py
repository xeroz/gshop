from django.urls import path
from .views import HomePageView, SearchResultView


app_name = 'web'

urlpatterns = [
    path(r'', HomePageView.as_view(), name='home'),
    path('search_result/', SearchResultView.as_view(), name='search_result'),
]
