from userprofile.serializers.ProfileSerializer import *
from userprofile.models.CustomUserModel import CustomUser
from userprofile.models.UserProfileModel import UserProfile
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class UserProfileAPIView(generics.ListAPIView):
	serializer_class = ProfileSerializer
	permission_classes = [IsAdminUser]
	def get_queryset(self):
		user_id = self.kwargs['userid']
		return UserProfile.objects.filter(user=user_id)		
		