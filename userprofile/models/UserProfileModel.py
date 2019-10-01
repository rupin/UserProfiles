from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class UserProfile(models.Model):
	profile_type=models.CharField(max_length=100, default='')
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		app_label="userprofile"
	def __str__(self):
		return self.profile_type
	



