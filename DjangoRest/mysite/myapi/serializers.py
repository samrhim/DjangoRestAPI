from rest_framework import serializers

from .models import Patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'firstname', 'lastname')

# serializers.py

#from rest_framework import serializers

#from .models import Hero

#class HeroSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Hero
#        fields = ( 'id', 'name', 'alias')
