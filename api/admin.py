from django.contrib import admin
from .models import Vehicle,counting, Phase, Roads, Spots
# Register your models here.

admin.site.register(Vehicle)
admin.site.register(counting)
admin.site.register(Phase)
admin.site.register(Roads)
admin.site.register(Spots)
