from django.shortcuts import render
from rest_framework import generics

# Create your views here.

class ProductView(generics.ListCreateAPIView):
    pass
