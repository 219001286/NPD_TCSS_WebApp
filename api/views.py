from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
def Home(request):
    context = { }
    return render(request, 'index.html' , context)

def Logout(request):
    context = { }
    return render(request, 'auth-pages/login.html')


def Register(request):
    context = { }
    return render(request, 'auth-pages/register.html')

def Forgetpwd(request):
    context = { }
    return render(request, 'components/password.html')

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)