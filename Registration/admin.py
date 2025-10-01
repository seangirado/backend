from django.contrib import admin

# This is the corrected line
from .models import UserRegistration

# You can now register your model with the admin site
admin.site.register(UserRegistration)