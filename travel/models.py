import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.

class City(models.Model):
	city_name = models.CharField(max_length=64)
	loc_lat = models.FloatField()
	loc_lon = models.FloatField()
	def __str__(self):
		return self.city_name
class BusCompany(models.Model):
	company_name = models.CharField(max_length=64)
	def __str__(self):
		return self.company_name
	def CompanyName(self):
		return company_name

class BusTrip(models.Model):
	review_title = models.CharField(max_length = 64,default = 'Review Title')
	author = models.CharField(max_length=64, default = 'Anonymous' ) #will eventually be set by logged in user
	bus_company = models.ForeignKey(BusCompany,on_delete=models.CASCADE)
	trip_date = models.DateField('date of trip')
	fare = models.IntegerField(default = 22000)
	fare.help_text = "=/ tsh"
	departure_time = models.TimeField(default=datetime.time(6))
	departure_city = models.ManyToManyField(City, related_name = 'departure_city')
	arrival_city = models.ManyToManyField(City, related_name = 'arrival_city')
	speed_choices = ((1,'1 - Pole Pole'),(2,'2 - Kama Kawaida'),(3,'3 - Faster than Usual'))
	speed = models.IntegerField(choices = speed_choices)
	safety_choices = ((1,'1 - Scary'),(2,'2 - On Par'),(3,'3 - Salama'))
	safety = models.IntegerField(choices = safety_choices)
	comfort_choices = ((1,'1 - Painful'),(2,'2 - Siyo Mbaya'),(3,'3 - Safi Sana'))
	comfort = models.IntegerField(choices = comfort_choices)
	review = models.TextField(max_length=500)
	review.blank = True
	recomendations = models.IntegerField(default=0) #upvotes
	def time_of_day(self):
		if datetime.time(5) <= self.departure_time < datetime.time(8):
			return 'Early Morning'
		if datetime.time(8) <= self.departure_time < datetime.time(12):
			return 'Late Morning'
		if datetime.time(12) <= self.departure_time < datetime.time(18):
			return 'Afternoon'
		else:
			return 'Nightime'
	def __str__(self):
		return self.review_title
		
class Committee(models.Model):
	committee_name = models.CharField(max_length = 64)
	def __str__(self):
                return self.committee_name+"Hi"
