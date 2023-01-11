from pickle import BINPERSID
from pkg_resources import BINARY_DIST
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from api.models import *
from rest_framework import generics
from .serializers import *
import datetime
from django.db.models import Count
# Create your views here.
class CountingCreateAPIView(generics.CreateAPIView):
    serializer_class = CountingSerializer
    permission_classes = (IsAuthenticated,)

# isplaying all registered vehicles 
class VehicleDetailAPIView(generics.ListAPIView):
    serializer_class = VehicleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        return queryset

# retrieving the counting for a spcific user who has logged in
class CountingDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CountingSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = counting.objects.filter(collector=self.request.user)
        return queryset



class PhaseListAPIView(generics.RetrieveAPIView):
    queryset = Phase.objects.all()
    serializer_class = PhaseSerializer
    # lookup_field = 'pk'
    # permission_classes = (IsAuthenticated,)

class RoadListAPIView(generics.ListAPIView):
    serializer_class = RoadSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Roads.objects.all()
        return queryset

class SpotListAPIView(generics.ListAPIView):
    serializer_class = SpotSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Spots.objects.all()
        return queryset