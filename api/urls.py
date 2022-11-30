from django.urls import path
from api import views

urlpatterns = [
      path('', views.Logout, name="Login"),
      path('Home', views.Home, name="home"),
      path('register', views.Register, name="register"),
      path('change-password', views.Forgetpwd, name="change-password"),

]