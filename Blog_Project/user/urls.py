from django.urls import path
from . import views
#sử dụng views có sẵn của django
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile'),
    path('', auth_views.LoginView.as_view(template_name = 'user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
]
