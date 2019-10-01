from userprofile.models.CustomUserModel import CustomUser
from userprofile.models.UserProfileModel import UserProfile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = UserProfile
		fields=['profile_type', 'user']		
		