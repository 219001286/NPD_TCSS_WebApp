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
from django.db.models import Count, Sum, Max
from .models import Phase, Vehicle, Roads, Spots, counting
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PhaseRegistrationForm, RoadRegistrationForm, SpotRegistrationForm, VehicleRegistrationForm
from django.db.models import Q




class TopVehicleCounterList( LoginRequiredMixin, ListView):
    template_name = 'dashboard/dashboard.html'
    model = CustomUser
    context_object_name = 'traffic_collector_list'

    def get_queryset(self):
        return CustomUser.objects.count()
    
    def get_context_data(self, *args, **kwargs):
        today = datetime.date.today()
        context = super().get_context_data(*args, **kwargs)
        total_traffic = counting.objects.aggregate(counts=Sum('Traffic_countings'))
        percentage = counting.objects.aggregate(perc = Sum('Traffic_countings') * 100/10000)
        daily_traffic = counting.objects.filter(updated__gt=today).aggregate(daily=Sum('Traffic_countings'))
        daily_counting = counting.objects.filter(updated__gt=today)
        top_vehicle_counted = counting.objects.aggregate(top_vehicle = Max('Traffic_countings'))['top_vehicle']
        high_counting_vehicles = counting.objects.filter(Traffic_countings=top_vehicle_counted)

        print(top_vehicle_counted)
       # context for displaying data on tampletes
        context['total_traffic'] = total_traffic
        context['percentage'] = percentage
        context['daily_traffic'] = daily_traffic
        context['daily_counting'] = daily_counting
        context['top_vehicle_counted'] = top_vehicle_counted
        context['high_counting_vehicles'] = high_counting_vehicles

        return context


# data from all surveyors 
class CollectedData( LoginRequiredMixin, ListView):
    template_name = 'components/display_data/collected_data.html'
    # model = CustomUser
    # paginate_by = 4
    # context_object_name = 'data_collector_list'

    def get_queryset(self):
        pass

class PhaseCreation(generic.CreateView, LoginRequiredMixin, ListView):
    form_class = PhaseRegistrationForm
    success_url = reverse_lazy('createphase')
    template_name = 'contents/phase.html'
    model = Phase
    context_object_name = 'phases'
    
    def get_queryset(self):
       today = datetime.date.today()
       queryset = Phase.objects.all()
       return queryset
 

class RoadCreation(generic.CreateView, LoginRequiredMixin, ListView):
    form_class = RoadRegistrationForm
    success_url = reverse_lazy('createroads')
    template_name = 'contents/roads.html'
    model = Roads
    context_object_name = 'roads'
    
    def get_queryset(self):
       today = datetime.date.today()
       queryset = Roads.objects.all()
       return queryset
 
class SpotCreation(generic.CreateView, LoginRequiredMixin, ListView):
    form_class = SpotRegistrationForm
    success_url = reverse_lazy('createspots')
    template_name = 'contents/spots.html'
    model = Spots
    context_object_name = 'spots'
    
    def get_queryset(self):
       today = datetime.date.today()
       queryset = Spots.objects.all()
       return queryset

class VehicleCreation(generic.CreateView, LoginRequiredMixin, ListView):
     form_class = VehicleRegistrationForm
     success_url = reverse_lazy('registervehicle')
     template_name = 'contents/vehicles.html'
     model = Vehicle
     context_object_name = 'vehicles'

     def get_queryset(self):
        today = datetime.date.today()
        queryset = Vehicle.objects.all()
        return queryset


class DataAnalysis( LoginRequiredMixin, ListView):
    template_name = 'contents/cleaning.html'

    def get_queryset(self):
        pass

class ProjectReport( LoginRequiredMixin, ListView):
    template_name = 'contents/report.html'

    def get_queryset(self):
        pass


# Displaying information from database  

class CollectorList( LoginRequiredMixin, ListView):
    template_name = 'collectors/list-collectors.html'

    def get_queryset(self):
        pass

class CollectorRegistration( LoginRequiredMixin, ListView):
    template_name = 'collectors/register_collectors.html'

    def get_queryset(self):
        pass


class TotalTraffic( LoginRequiredMixin, ListView):
    template_name = 'dashboard/dashboard.html'
    model = counting
    context_object_name = "traffic_counted_total"

    def get_queryset(self):
        queryset = counting.objects.aggregate(Sum('Traffic_countings'))
        return queryset

# search field 
def searchvehicle(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= counting.objects.filter(Q(created__icontains=query) | Q(updated__icontains=query)).distinct()

            context={'results': lookups,
                     'submitbutton': submitbutton}

            return render(request, 'contents/search.html', context)

        else:
            return render(request, 'contents/search.html')

    else:
        return render(request, 'search/search.html')






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