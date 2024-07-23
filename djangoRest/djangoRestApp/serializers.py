from rest_framework import serializers
from .models import RawData, NewData

class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = '__all__'

class NewDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewData
        fields = '__all__'
