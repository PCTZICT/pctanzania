from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone


def index(request):
	return HttpResponse("shit will be here shortly")
def buses(request):
	return HttpResponse("bus shit will be here shortly")
	