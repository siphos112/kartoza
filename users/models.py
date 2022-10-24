from enum import unique
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
	'''
	UserProfile model extends the built-in Django User Model
	'''
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	address = models.CharField(verbose_name="Street Address",max_length=100, null=True, blank=True)
	complex_building = models.CharField(verbose_name="Complex/Building", max_length=100, null=True, blank=True)
	suburb = models.CharField(verbose_name="Suburb", max_length=100, null=True, blank=True)
	town = models.CharField(verbose_name="Town/City", max_length=100, null=True, blank=True)
	province = models.CharField(verbose_name="Province", max_length=100, null=True, blank=True)
	post_code = models.CharField(verbose_name="Post Code", max_length=8, null=True, blank=True)
	country = models.CharField(verbose_name="Country", max_length=100, null=True, blank=True)
	longitude = models.CharField(verbose_name="Longitude", max_length=50, null=True, blank=True)
	latitude = models.CharField(verbose_name="Latitude", max_length=50, null=True, blank=True)

	captcha_score = models.FloatField(default = 0.0)
	has_profile = models.BooleanField(default = False)
	
	is_active = models.BooleanField(default = True)

	def __str__(self):
		return f'{self.user}'


class LoginActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + " logged in on " + str(self.date)

class LogoutActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + " logged out on " + str(self.date)