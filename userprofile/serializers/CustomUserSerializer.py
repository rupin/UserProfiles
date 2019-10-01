from userprofile.models.CustomUserModel import CustomUser
from userprofile.models.UserProfileModel import UserProfile
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = CustomUser		
		fields=['id','username', 'email']

class CustomUserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	

	class Meta:
		model = CustomUser		
		fields=['id', 'username', 'password', 'email',]

	def create(self, validated_data):
		user = super(CustomUserCreateSerializer, self).create(validated_data)
		user.set_password(validated_data['password'])
		user.is_active=True
		user.is_superuser=False
		user.is_staff=False
		user.save()

		#add profiles for the User
		officer=UserProfile(profile_type="Officer", user=user)
		officer.save()

		admin=UserProfile(profile_type="Admin", user=user)
		admin.save()

		return user

class CustomUserDeleteSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = CustomUser


class CustomUserUpdateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = CustomUser		
		fields=['first_name', 'last_name']

class PDFSerializer(serializers.ModelSerializer):
	pdfbase64=serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
	
	class Meta:
		model = CustomUser		
		fields=['pdfbase64']

	
        

	
	

	

		