from django.contrib import admin

# Register your models here.
from .models import BusTrip, City, BusCompany

class BusTripAdmin(admin.ModelAdmin):
	list_display = ('review_title' ,'bus_company', 'time_of_day', 'trip_date','fare')
	list_filter = ['departure_city','arrival_city',]

admin.site.register(BusTrip, BusTripAdmin)
admin.site.register(City)
admin.site.register(BusCompany)
