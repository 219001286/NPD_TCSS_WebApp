from django import forms
from .models import Phase, Roads, Spots, Vehicle


class PhaseRegistrationForm(forms.ModelForm):
  
    class Meta:
        model = Phase
        fields = "__all__"

class RoadRegistrationForm(forms.ModelForm):
  
    class Meta:
        model = Roads
        fields = "__all__"

class SpotRegistrationForm(forms.ModelForm):
  
    class Meta:
        model = Spots
        fields = "__all__"


class VehicleRegistrationForm(forms.ModelForm):
  
    class Meta:
        model = Vehicle
        fields = "__all__"