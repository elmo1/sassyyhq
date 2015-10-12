from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from django.template import loader, Context
from landing.forms import SignupForm

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	else: 
		form = SignupForm()
	return render(request, 'index.html', {'form': form})