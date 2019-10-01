from userprofile.serializers.ProfileSerializer import *
from userprofile.models.CustomUserModel import CustomUser
from userprofile.models.UserProfileModel import UserProfile
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import NotFound
class UserProfileAPIView(generics.ListAPIView):
	serializer_class = ProfileSerializer
	permission_classes = [IsAdminUser]
	def get_queryset(self):
		user_id = self.kwargs['userid']
		data=UserProfile.objects.filter(user=user_id)
		if(data.count()==0):
			raise NotFound
		return data		
		