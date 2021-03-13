from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User


# Create your views h
def home(request):
	title = "Welcome To Lost and Found"
	return render(request, 'found/home.html', {'title': title})

@login_required
def found_form(request):
	if request.method == 'POST':
		#form = ProductFoundForm(request.POST.body)
		#print(request.POST)
		form = ProductFoundForm(request.POST)
		if form.is_valid():
			form.instance.person = request.user
			form.save()
			messages.success(request,f'Item is successfully added')
			return redirect('l&f-home')
		else:
			form = ProductFoundForm()
			title = "Register Missing Article"
			return render(request, 'found/foundform.html', {'form': form, 'title': title})
	else:
		form = ProductFoundForm()
		title = "Register Missing Article"
		return render(request, 'found/foundform.html', {'form': form, 'title': title})

def find_item(request):
	title = "Find Lost Item"
	return render(request, 'found/find_item.html', {'title': title})