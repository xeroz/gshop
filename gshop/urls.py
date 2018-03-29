from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import (
    password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete
)


url_password_reset = {
    'template_name':'shop/auth/password/send_email.html',
    'email_template_name':'shop/auth/password/reset_email.html'
}
url_password_done = {
    'template_name':'shop/auth/password/reset_done.html'
}
url_password_confirm = {
    'template_name': 'shop/auth/password/reset_confirm.html'
}
url_done = {
    'template_name': 'shop/auth/password/reset_complete.html'
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path(r'', include('apps.web.urls', namespace='web')),
    path(r'', include('apps.products.urls', namespace='products')),
    path(r'', include('apps.users.urls', namespace='users')),
    path(r'', include('apps.auth.urls', namespace='auth')),
    url(r'^froala_editor/', include('froala_editor.urls')),
    url('', include('social_django.urls', namespace='social')),
    path(r'reset/password/$', password_reset,
        url_password_reset, name='password_reset'
    ),
    path(r'reset/password_done/$', password_reset_done,
        url_password_done, name='password_reset_done'
    ),
    path(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        url_password_confirm, name='password_reset_confirm'
    ),
    path(r'reset/done', password_reset_complete,
        url_done, name='password_reset_complete'
),
]
