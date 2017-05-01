from django.contrib import admin
from .models import User, Workshop

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ["first_name","last_name","email"]
	search_fields = ['first_name', 'last_name',"email"]

class WorkshopAdmin(admin.ModelAdmin):
	list_display = ("first_name", 'last_name',  'FridayWorkshop', 'SaturdayWorkshop')
	list_filter = ('FridayWorkshop', )

admin.site.register(User,UserAdmin)
admin.site.register(Workshop,WorkshopAdmin)

