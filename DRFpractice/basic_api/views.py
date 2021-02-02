from django.shortcuts import render
from rest_framework import generics
from .models import DRFPost
from .serializers  import DRFPostSerializer
# from .serializers import DRFPostSerializer
# Create your views here.

class API_objects(generics.ListCreateAPIView):
    queryset = DRFPost.object.all()
    serializer_class = DRFPostSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer

