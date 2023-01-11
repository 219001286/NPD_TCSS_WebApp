
from django.urls import path, include
from .views import *

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('', auth_views.LoginView.as_view(template_name='auth-pages/login.html', redirect_authenticated_user=True),
         name='login'),
    path('signup/', SignupPageView.as_view(), name='signup')
]       