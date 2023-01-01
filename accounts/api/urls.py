from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from accounts.api.views import AccountRegistrationView, AccountLogoutView

urlpatterns = [
    path('', obtain_auth_token, name='login'),
    path('register/', AccountRegistrationView, name='createUser'),
    path('logout/', AccountLogoutView, name='logout'),
]