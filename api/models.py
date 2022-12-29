from django.db import models
from accounts.models import CustomUser
    

# the categories of the vehicles used 
VehicleChoice = (
    ('Motorcycle','Motorcycle'),
    ('Cars','Cars'),
    ('Utility','Utility'),
    ('Microbus','Microbus'),
    ('Minibus','Minibus'),
    ('Large buses','Large buses'),
    ('Light Truck','Light Truck'),
    ('Medium Truck','Medium Truck'),
    ('Heavy Truck','Heavy Truck'),
    ('Trailer and Trailer Trucks', 'Trailer and Trailer Trucks'),
    ('Bicycle','Bicycle'),
    ('Tempo','Tempo'),
   
)

# vehicles
class Vehicle(models.Model):
    vehicle_category = models.CharField(max_length=100, choices=VehicleChoice)
    vehicle_image = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created'] 

    def __str__(self):
        return (self.vehicle_category)

# counting vehicles
class counting (models.Model):
    collector = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name="collector_vehicles", null=True)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created'] 

    def __str__(self):
        return (self.count)


# phase : District will be used as location
class Phase(models.Model):
    Phase_name = models.CharField(max_length=10)
    Phase_location = models.CharField(max_length=10)  
    Starting_date = models.DateTimeField()
    Ending_date = models.DateTimeField()
    class Meta:
        ordering = ['-Ending_date', '-Starting_date'] 

    def __str__(self):
        return (self.count)

 
# Roads : the which will be constructed during the specified phase
class Roads(models.Model):
    Road_name = models.CharField(max_length=100)
    Phase = models.ForeignKey('Phase', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created'] 

    def __str__(self):
        return (self.Road_name)

# Spots: the spots for all data collectors working on specific road
class Spots(models.Model):
    Spot_name = models.CharField(max_length=50)
    Spot_code = models.CharField(max_length=50)
    Roads = models.ForeignKey('Roads', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created'] 

    def __str__(self):
        return (self.Spot_name)

