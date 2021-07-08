from rest_framework import serializers
from . import models


class CarListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = models.Car
        fields = '__all__'


class CarDetailSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = models.Car
        fields = '__all__'
