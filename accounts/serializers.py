from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, allow_blank=True, required=False)
    password_confirmation = serializers.CharField(write_only=True, allow_blank=True, required=False)

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'phone_number', 'address', 'image', 'level','password', 'password_confirmation')

    def create(self, validated_data):
        print("create")
        if validated_data['password'] == "":
            raise serializers.ValidationError({"password": "This field is required"})
        if validated_data['password'] != validated_data['password_confirmation']:
            raise serializers.ValidationError({"password_confirmation": "Password fields did not match."})
        user = CustomUser.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            level=validated_data.get('level'),
            phone_number=validated_data.get('phone_number'),
            address=validated_data.get('address'),
            image=self.context.get('view').request.FILES.get('image'),
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    
    def update(self, instance, validated_data):
        print(validated_data)
        for key, value in validated_data.items():
            if key != 'image':
                setattr(instance, key, value)
            else:
                image = self.context.get('view').request.FILES.get('image')
                if image:
                    setattr(instance, key, image)
        instance.save()
            
        return instance

