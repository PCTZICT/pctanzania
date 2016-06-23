from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class HomepageView(LoginRequiredMixin, generic.TemplateView):
	login_url = '/accounts/login/'
	redirect_field_name = 'redirect_to'
	template_name = "index/index.html"
	