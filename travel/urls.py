from django.conf.urls import url

from . import views

app_name = 'travel'
urlpatterns = [
	# /travel/
	url(r'^$',views.index, name='index'),
	#/travel/iringa/
	# url(r'^(?P<city_name>\w+)/$',views.city, name='city'), #[a-zA-Z0-9_]
	#
	url(r'^buses/$',views.buses, name='buses'),
	
	# /polls/5/
	# url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	# /polls/5/results/
	# url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	#/polls/5/vote/
	# url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	
]