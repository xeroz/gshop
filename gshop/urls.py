from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path(r'', include('apps.web.urls', namespace='web')),
    path(r'', include('apps.products.urls', namespace='products')),
    path(r'', include('apps.users.urls', namespace='users')),
    path(r'', include('apps.auth.urls', namespace='auth')),
    url(r'^froala_editor/', include('froala_editor.urls')),
    url('', include('social_django.urls', namespace='social')),
]
