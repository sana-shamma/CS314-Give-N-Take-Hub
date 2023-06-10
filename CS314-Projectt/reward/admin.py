

# Register your models here.
from django.contrib import admin
from .models import UserProfile, Coupon

admin.site.register(UserProfile)
admin.site.register(Coupon)