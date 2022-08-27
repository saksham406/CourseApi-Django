from rest_framework import serializers 
from . models import Course 

class CourserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','name','language','price')
