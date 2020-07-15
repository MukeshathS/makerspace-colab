from django.conf.urls import url
from . import views
# from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

# PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views
# import requests
from django.urls import path

app_name = "users"

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='profile/login.html', extra_content={'user': 'Hello Guest!'}), name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='profile/registration/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='profile/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='profile/registration/password_reset_form.html'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='profile/registration/password_reset_complete.html'),
     name='password_reset_complete'),
]
