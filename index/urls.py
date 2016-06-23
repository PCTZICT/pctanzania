from django.conf.urls import url

from . import views

app_name = 'index'
urlpatterns = [
	url(r'^$', views.HomepageView.as_view(), name='index'),


]