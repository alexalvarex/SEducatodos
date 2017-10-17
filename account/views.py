from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import MyAuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/principal/')
		
	form = MyAuthenticationForm()
	return render(request, 'form_login.html', {'form': form})

def blockscreen(request):		
	form = MyAuthenticationForm()
	username = request.user.get_username()
	logout(request)
	return render(request, 'blockscreen.html', {'form': form, 'username': username})

@login_required()
def myprofile(request):
	return render(request, 'myprofile.html')
	
@login_required()
def changepass(request):
	return render(request, 'changepass.html')

def forgotpass(request):
	return render(request, 'forgotpass.html')


def log_out(request):
	logout(request)
	return HttpResponseRedirect('/')

def log_in_error(request):
	form = MyAuthenticationForm()
	return render(request, 'form_login_error.html', {'form': form})

def log_in_inactive(request):
	form = MyAuthenticationForm()
	return render(request, 'form_login_inactive.html', {'form': form})

def log_in(request):
	if request.method == 'POST':
		form = MyAuthenticationForm(data=request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
			if user is not None:
				if user.is_active:
					login(request, user)
					if user:
						return HttpResponseRedirect('/principal/')
				else:
					return HttpResponseRedirect('/account/login/inactive/')
			else:
				return HttpResponseRedirect('')
		else:
			return HttpResponseRedirect('/account/login/error/')
	else:
		return HttpResponseRedirect('/')
