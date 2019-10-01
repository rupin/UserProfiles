from userprofile.serializers.CustomUserSerializer import *
from userprofile.models.CustomUserModel import CustomUser

from userprofile.utils.renderPDF import render_to_pdf

from rest_framework.viewsets import *
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse


from rest_framework import generics


from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework.mixins import DestroyModelMixin

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.status import * 

from rest_framework.exceptions import NotFound
from rest_framework.throttling import UserRateThrottle


		
class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]

class ListUsersAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

class deleteUserAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
	serializer_class = CustomUserDeleteSerializer
	permission_classes = [IsAdminUser]
	throttle_classes = [UserRateThrottle]

	def get_queryset(self):        
		return CustomUser.objects.all()	

	def delete(self, request, *args, **kwargs):
		#print(kwargs)
		return self.destroy(request, *args, **kwargs)


class UpdateUserAPIView(generics.UpdateAPIView):
	serializer_class = CustomUserUpdateSerializer
	permission_classes = [IsAdminUser]

	def get_queryset(self):        
		return CustomUser.objects.all()
		
	def update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return Response(serializer.data)

class GeneratePDFView(APIView):
	serializer_class=PDFSerializer
	permission_classes = [IsAdminUser]
	throttle_classes = [UserRateThrottle]

	def get(self, request, **kwargs):
		userID=kwargs['pk']
		data=CustomUser.objects.filter(id=userID)
		if(data.count()==0):
			raise NotFound
		context={"data":data}
		errorcode=HTTP_200_OK
		pdf = render_to_pdf('template_pdf.html', context)
		status=[]
		newOBJ={}
		newOBJ["pdfbase64"]=pdf
		status.append(newOBJ)
		
		return Response(status, status=errorcode)

		

	
	
	
	