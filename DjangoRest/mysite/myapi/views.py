#from django.shortcuts import render

#from rest_framework import viewsets

#from .serializers import HeroSerializer
#from .models import Hero


#class HeroViewSet(viewsets.ModelViewSet):
#    queryset = Hero.objects.all().order_by('name')
#    serializer_class = HeroSerializer
# Create your views here.


from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PatientSerializer
from .models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('id')
    serializer_class = PatientSerializer

