from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from time import timezone
import xlwt
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from accounts.models import CustomUser
import datetime
from django.db.models import Count, Sum
from .models import Phase, Vehicle
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PhaseRegistrationForm, RoadRegistrationForm, SpotRegistrationForm, VehicleRegistrationForm
# Create your views here.

class TopVehicleCounterList( LoginRequiredMixin, ListView):
    template_name = 'dashboard/dashboard.html'
    # model = CustomUser
    # paginate_by = 4
    # context_object_name = 'data_collector_list'

    def get_queryset(self):
        pass
    #     return CustomUser.objects.filter(collector_species__status="approved", is_staff=False).annotate(
    #         num_approved=Count('collector_species__status'), )

    # def get_context_data(self, *args, **kwargs):
    #     today = datetime.date.today()
    #     context = super().get_context_data(*args, **kwargs)
    #     count_approved = Species.objects.filter(status='approved').count()
    #     count_rejected = Species.objects.filter(status='rejected').count()
    #     entry_count = Species.objects.filter(updated_at__gt=today,status='approved').count()
    #     count_pending = Species.objects.filter(status='pending').count()
    #     context['count_approved'] = count_approved
    #     context['count_rejected'] = count_rejected
    #     context['entries_count'] = entry_count
    #     context['pending_count'] = count_pending

    #     return context


# data from all surveyors 
class CollectedData( LoginRequiredMixin, ListView):
    template_name = 'components/display_data/collected_data.html'
    # model = CustomUser
    # paginate_by = 4
    # context_object_name = 'data_collector_list'

    def get_queryset(self):
        pass

class PhaseCreation(generic.CreateView):
    form_class = PhaseRegistrationForm
    success_url = reverse_lazy('createphase')
    template_name = 'contents/phase.html'
 

class RoadCreation(generic.CreateView):
    form_class = RoadRegistrationForm
    success_url = reverse_lazy('createroads')
    template_name = 'contents/roads.html'
 
class SpotCreation(generic.CreateView):
     form_class = SpotRegistrationForm
     success_url = reverse_lazy('createspots')
     template_name = 'contents/spots.html'

class VehicleCreation(generic.CreateView):
     form_class = VehicleRegistrationForm
     success_url = reverse_lazy('registervehicle')
     template_name = 'contents/vehicles.html'



class DataAnalysis( LoginRequiredMixin, ListView):
    template_name = 'contents/cleaning.html'

    def get_queryset(self):
        pass

class ProjectReport( LoginRequiredMixin, ListView):
    template_name = 'contents/report.html'

    def get_queryset(self):
        pass


# Displaying information from database
class VehicleList(ListView):
    model = Vehicle
    template_name = 'contents/vehicles.html'
    context_object_name = 'vehicles'

    def get_queryset(self):
        today = datetime.date.today()
        queryset = Vehicle.objects.all()
        return queryset

class CollectorList( LoginRequiredMixin, ListView):
    template_name = 'collectors/list-collectors.html'

    def get_queryset(self):
        pass

class CollectorRegistration( LoginRequiredMixin, ListView):
    template_name = 'collectors/register_collectors.html'

    def get_queryset(self):
        pass




# def Home(request):
#     context = { }
#     return render(request, 'index.html' , context)

# def Logout(request):
#     context = { }
#     return render(request, 'auth-pages/login.html')


# def Register(request):
#     context = { }
#     return render(request, 'auth-pages/register.html')

# def Forgetpwd(request):
#     context = { }
#     return render(request, 'components/password.html')

# class HelloView(APIView):
#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)