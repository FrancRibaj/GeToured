from django.contrib import admin
from .models import CustomUser,Traveler,Agency
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Traveler)
admin.site.register(Agency)
