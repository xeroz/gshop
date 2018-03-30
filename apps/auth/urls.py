from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'auth'

url_password_reset = {
    'template_name': 'shop/auth/password/send_email.html',
    'email_template_name': 'shop/auth/password/reset_email.html'
}
url_password_done = {
    'template_name': 'shop/auth/password/reset_done.html'
}
url_password_confirm = {
    'template_name': 'shop/auth/password/reset_confirm.html'
}
url_done = {
    'template_name': 'shop/auth/password/reset_complete.html'
}
urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             template_name='shop/auth/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(next_page='/'),
         name='logout'),
    path('reset/password/',
         auth_views.PasswordResetView.as_view(
             email_template_name='shop/auth/password/reset_email.html',
             html_email_template_name='shop/auth/password/reset_email.html',
             template_name='shop/auth/password/send_email.html',
             success_url=reverse_lazy('auth:password_reset_done'),
         ),
         name='password_reset'),
    path('reset/password_done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='shop/auth/password/reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='shop/auth/password/reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='shop/auth/password/reset_complete.html'),
         name='password_reset_complete'),
]
