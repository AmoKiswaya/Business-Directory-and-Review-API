from django.shortcuts import render
from rest_framework import generics, filters
from .models import Business
from .serializers import BusinessSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BusinessListView(generics.ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer 

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ['name', 'description', 'location']
    filterset_fields = ['category', 'owner', 'location']
    ordering_fields = ['name', 'created_at'] 

