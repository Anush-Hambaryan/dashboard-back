from rest_framework import serializers
from .models import StandardJob, Job5, Coords

from accounts.models import CustomUser

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['lat', 'lng']

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'level' ]

class StandardJobSerializer(serializers.ModelSerializer):
    coords = CoordsSerializer(source="coords_stantdard_job", many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = StandardJob
        fields = ['id', 'owner', 'created', 'job_type', 'address', 'status', 'coords']
    
    def create(self, validated_data):
        coords_data = validated_data.pop('coords_stantdard_job')
        job = StandardJob.objects.create(**validated_data)
        if coords_data:
            for coords in coords_data:
                Coords.objects.create(standard_owner=job, **coords)
        return job


class Job5Serializer(serializers.ModelSerializer):
    coords = CoordsSerializer(source='coords_job5', many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Job5
        fields = ['id','owner', 'created','shape','radius', 'coords',]
    
    def create(self, validated_data):
        coords_data = validated_data.pop('coords_job5')
        job = Job5.objects.create(**validated_data)
        if coords_data:
            for coords in coords_data:
                Coords.objects.create(job5_owner=job, **coords)
        return job