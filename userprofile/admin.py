from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from userprofile.models.CustomUserModel import CustomUser
from userprofile.models.UserProfileModel import UserProfile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]



	

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)