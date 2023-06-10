from django.contrib import admin
from . models import borrowedItem,swapedItem,giftItem

# Register your models here.

# Database For Borrowed Item
admin.site.register(borrowedItem)

# Database For Swaped Item
admin.site.register(swapedItem)

# Database For Gift Item
admin.site.register(giftItem)