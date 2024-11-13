from django.contrib import admin
from . models import Item
# Register your models here.

# admin.site.register(Item)

class ItemAdmin(admin.ModelAdmin):
    # Yeh dono fields admin panel mein dikhai denge
    list_display = ("id", 'name', 'description')  

# Item model ko admin panel mein register karte hain
admin.site.register(Item, ItemAdmin)