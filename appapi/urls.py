from django.urls import include, path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views
schema_view = get_schema_view(
    openapi.Info(
        title="NPD Traffic Counting",
        default_version='v1',
        description="API App for collecting traffic data collection",      
        terms_of_service="https://yourco/terms/",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Private"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('account/',include('accounts.api.urls')),
    path('counting/', views.CountingCreateAPIView.as_view(), name='couting'),
    path('vehicles-detail/', views.VehicleDetailAPIView.as_view(), name='vehicle-list'),
    path('phase/<int:pk>/', views.PhaseListAPIView.as_view(), name='phase'),
    path('road/', views.RoadListAPIView.as_view(), name='road'),
    path('spot/', views.SpotListAPIView.as_view(), name='spot'),
    path('counting-detail/<int:pk>/', views.CountingDetailAPIView.as_view(), name='counting-detail'),
    # path('list/today-counted-vehicles/', views.TodayCountedVehiclesListAPIView.as_view(), name='today-registered'                                                                                           '-specie-list'),
  


]