from django.contrib import admin
from . models import LogoutActivity, LoginActivity


admin.site.register(LoginActivity)
admin.site.register(LogoutActivity)