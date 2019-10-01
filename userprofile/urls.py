"""userprofile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from userprofile.apiviews.CustomUserAPIView import *
from userprofile.apiviews.UserProfileAPIViews import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_auth.urls')),
    path('api/addUser/', UserCreateAPIView.as_view(), name='adduser'),
    path('api/listUsers/', ListUsersAPIView.as_view()),
    path('api/deleteUser/<int:pk>/', deleteUserAPIView.as_view()),
    path('api/updateUserDetails/<int:pk>/', UpdateUserAPIView.as_view()),
    path('api/listProfiles/<int:userid>/', UserProfileAPIView.as_view()),
    path('api/show-pdf/<int:pk>', GeneratePDFView.as_view()),
]
