from django.urls import path
from api import views
from .views import (searchvehicle)

urlpatterns = [

      # inserting data endpoints
      path('dashboard', views.TopVehicleCounterList.as_view(), name='dashboard'),
      path('overall-data', views.CollectedData.as_view(), name='overalldata'),
      path('create-phase', views.PhaseCreation.as_view(), name='createphase'),
      path('create-roads', views.RoadCreation.as_view(), name='createroads'),
      path('create-spots', views.SpotCreation.as_view(), name='createspots'),
      path('register-vehicle', views.VehicleCreation.as_view(), name='registervehicle'),
      path('collector-register', views.CollectorRegistration.as_view(), name='collectorregister'),
      path('collector-list', views.CollectorList.as_view(), name='collectorlist'),
      path('clean-data', views.DataAnalysis.as_view(), name='cleandata'),
      path('report', views.ProjectReport.as_view(), name='report'),

      # search 
      path('search/result', searchvehicle, name='searchvehicle'),


      # retrieving data from 
     
]