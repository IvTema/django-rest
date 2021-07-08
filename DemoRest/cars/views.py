from django.shortcuts import render
from rest_framework import generics
from . import serializers, models, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class CarCreateView(generics.CreateAPIView):
    serializer_class = serializers.CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = serializers.CarListSerializer
    queryset = models.Car.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CarDetailSerializer
    queryset = models.Car.objects.all()
    permission_classes = (permissions.IsOwnerOrReadOnly, IsAdminUser)


