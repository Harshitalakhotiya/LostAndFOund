from django.shortcuts import render, redirect
from .forms import *

# Create your views h
def home(request):
	title = "Welcome To Lost and Found"
	return render(request, 'found/home.html', {'title': title})

def found_form(request):
	if request.method == 'POST':
		form_data = {

		}
		#form = ProductFoundForm(request.POST.body)
		#print(request.POST)
		form = ProductFoundForm(request.POST)
		return redirect('l&f-home')
	else:
		form = ProductFoundForm()
		title = "Register Missing Article"
		return render(request, 'found/foundform.html', {'form': form, 'title': title})

def find_item(request):
	title = "Find Lost Item"
	return render(request, 'found/find_item.html', {'title': title})