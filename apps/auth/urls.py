from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import (
    login, logout,
    password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete
)

app_name = 'auth'

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
    path('login/', login, {'template_name': 'shop/auth/login.html'}, name='login'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),
    # path('reset/password/', password_reset,
    #      url_password_reset, name='password_reset'),
    # url('reset/password_done/', password_reset_done,
    #      url_password_done, name='password_reset_done'),
    # path('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/', password_reset_confirm,
    #     url_password_confirm, name='password_reset_confirm'
    #     ),
    # path('reset/done', password_reset_complete,
    #     url_done, name='password_reset_complete'
    #     ),
]
