from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User

def home(request):
	title = "Welcome To Lost and Found"
	return render(request, 'found/home.html', {'title': title})

@login_required
def found_form(request):
	print(request.session)
	if request.method == 'POST':
		#print(request.POST.get('x'))
		form = ProductFoundForm(request.POST)
		if form.is_valid():
			form.instance.person = request.user
			this_item = form.save()
			this_item.x = request.session.get('x', 0.0)
			this_item.y = request.session.get('y', 0.0)
			this_item.save()

			messages.success(request,f'Item is successfully added')
			context = {
				'id': this_item.id,
			}
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

def index(request):
	if request.method == 'POST':
		print('HEREEEE')
		xv = request.POST.get('fname')
		print('xv')
		yv = request.POST.get('lname')
		print('HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
		context = {
			'x'  : xv,
			'y' : yv
		}

		request.session['x'] = xv
		request.session['y'] = yv
		#return render(request, 'foundform', context)
		return redirect('foundform')
		# return JsonResponse({"xvar":xv,"yvar":yv})
	else:
		return render(request, 'found/map.html')