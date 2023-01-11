from rest_framework import serializers
from api.models import Vehicle, Phase, Roads, Spots, counting


class VehicleSerializer(serializers.ModelSerializer):
    # collector_name = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # sampling_date = serializers.DateTimeField(format=("%Y-%m-%d"),)
    class Meta:
        model = Vehicle
        fields = '__all__'


class CountingSerializer(serializers.ModelSerializer):
    collector = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # sampling_date = serializers.DateTimeField(format=("%Y-%m-%d"),)
    class Meta:
        model = counting
        fields = '__all__'

class PhaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phase
        fields = '__all__'

class SpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spots
        fields = '__all__'

class RoadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roads
        fields = '__all__'
