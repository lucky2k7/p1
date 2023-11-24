from django.contrib import admin
from city.models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ('city_tital','city_description')

# Register your models here.
admin.site.register(City,CityAdmin)
