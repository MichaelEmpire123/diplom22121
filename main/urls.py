from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), # Используем наше представление
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.change_profile, name='change_data'),
]